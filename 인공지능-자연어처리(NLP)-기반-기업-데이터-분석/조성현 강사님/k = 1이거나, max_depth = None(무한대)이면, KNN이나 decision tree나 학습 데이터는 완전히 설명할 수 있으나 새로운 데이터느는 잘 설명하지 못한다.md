k = 1이거나, max_depth = None(무한대)이면, KNN이나 decision tree나 학습 데이터는 완전히 설명할 수 있으나 새로운 데이터느는 잘 설명하지 못한다. 

한편, k가 너무 작거나 max_depth가 너무 작아도 과소적합이다.



KNN의 경우, k값에 따라 accuracy를 측정한다. k가 너무 작으면 underfitting. k가 증가할수록 accuracy 증가하다가, 어느 정도를 넘어 가면 시험 데이터의 accuracy가 다시 감소하는 현상. 그래서 시험 데이터를 가장 잘 설명할 수 있는 위치를 판단해야 한다. 



decision tree에서도 마찬가지로 depth에 대해 이야기해볼 수 있다. depth가 너무 작으면 