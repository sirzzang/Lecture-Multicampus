# Unrolled GAN library - Generator가 사용할 Surrogate loss function (fk)을 생성한다.
#
# 원 논문 : Luke Metz, et, al., 2016, Unrolled Generative Adversarial Network
# 아래 코드는 논문의 저자인 Google Brain 팀의 Luke Metz등이 작성한 코드의 일부임.
# 코드 URL : https://github.com/poolio/unrolled_gan
#
# 이 코드를 MyUtil/UnrolledGAN에 넣고 library 처럼 활용하기로 함.
#
# 2018.9.15, 아마추어퀀트 (조성현)
# ---------------------------------------------------------------------------------
from collections import OrderedDict
from keras.optimizers import Adam
import tensorflow as tf

def graph_replace(*args, **kwargs):
    graph = tf.get_default_graph()
    for op in graph.get_operations():
        op._original_op = None
    return tf.contrib.graph_editor.graph_replace(*args, **kwargs)

def extract_update_dict(update_ops):
    name_to_var = {v.name: v for v in tf.global_variables()}
    updates = OrderedDict()
    for update in update_ops:
        var_name = update.op.inputs[0].name
        var = name_to_var[var_name]
        value = update.op.inputs[1]
        if update.op.type == 'Assign':
            updates[var.value()] = value
        elif update.op.type == 'AssignAdd':
            updates[var.value()] = var + value
        else:
            raise ValueError("Update op type (%s) must be of type Assign or AssignAdd" % update.op.type)
    return updates

def SurrogateLoss(theta_d, loss_d, unrolled_k):
    D_update = Adam(lr=0.0001).get_updates(theta_d, [], loss_d)
    train_d = tf.group(*D_update, name="train_d")
    
    if unrolled_k > 0:
        # Get dictionary mapping from variables to their update value after one optimization step
        update_dict = extract_update_dict(D_update)
        cur_update_dict = update_dict
        
        for i in range(unrolled_k - 1):
            # Compute variable updates given the previous iteration's updated variable
            cur_update_dict = graph_replace(update_dict, cur_update_dict)
            
        # Final unrolled loss uses the parameters at the last time step
        loss_g = graph_replace(loss_d, cur_update_dict)
    else:
        loss_g = loss_d
        
    return train_d, loss_g