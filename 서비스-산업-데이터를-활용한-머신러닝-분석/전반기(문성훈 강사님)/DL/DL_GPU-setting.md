# Deep Learning 환경설정

nvidia만 지원해준다.

```BASH
어떻게 내 그래픽 카드 확인하지?
=> 장치 관리자 => 디스플레이 어댑터
```

![image-20200110094850280](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200110094850280.png)

## 1. 새로운 가상환경 생성 : gpu_env 

```python
# 아나콘다 프롬프트 창에
# (base) conda create -n gpu_env python=3.6 openssl
# activate gpu_env
# conda install nb_conda
# python -m ipykernel install --user --name=gpu_env --display-name=[GPU_ENV]
```

#### 1 ) jupyter notebook에 GPU_ENV가 생성된다.

![image-20200110101721250](images/image-20200110101721250.png)

#### 2 ) jupyter notebook에서 kernel을 바꿔 이제 gpu_env에서 작업을하자 !

![image-20200110102008014](images/image-20200110102008014.png)

#### 3 ) module 설치

: gpu_env에는 pandas를 설치한 적이 없기 때문에 error가 발생한다.

사용하는 모듈을 다시 설치하자

![image-20200110102432055](images/image-20200110102432055.png)



## 설치

#### 0 ) fileserver에서 폴더 다운로드

* 메일로 파일이 안보내진다....... USB 필요해!

![image-20200110094312084](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200110094312084.png)

```python
1 ) 441.87 =  grapic device
2 ) 설치
3 ) 설치
```

#### 1 ) 441.87 비디오드라이버 설치

![image-20200110100546530](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200110100546530.png)

![image-20200110100721684](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200110100721684.png)

![image-20200110100819045](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200110100819045.png)

#### 2 ) cuda  : 버전을 잘 맞춰주어야한다.

![image-20200110102228696](images/image-20200110102228696.png)

![image-20200110102526872](images/image-20200110102526872.png)

![image-20200110102543179](images/image-20200110102543179.png)

![image-20200110102638980](images/image-20200110102638980.png)

![image-20200110102653885](images/image-20200110102653885.png)

![image-20200110102714697](images/image-20200110102714697.png)

![image-20200110102833176](images/image-20200110102833176.png)

=> 실패하면 기존에 NVDIA 드라이버가 설치되어있었던것과 충돌이 난 것이다. 

![image-20200110111533646](images/image-20200110111533646.png)

위의 441.37을 삭제한 후 컴퓨터 재부팅,

그리고 다시 1)로 돌아가서 설치하자

#### 3 ) cudnn 압축을 풀어서 덮어쓴다

![image-20200110111337882](images/image-20200110111337882.png)

```python
#가상환경에 필요한 모듈 설치
새로운 아나콘다 프롬프트 창에 gpu_env에서
pip install pandas
pip install numpy
pip install matplotlib
# cuda 버전과 똑같은 tensorflow를 설치해야한다.
pip install tensorflow-gpu==1.15
```

