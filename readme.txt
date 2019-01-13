训练过程中，基本使用jupyter notebook
agents.py包含自己的agents类Best_agent
board.py包含棋盘one hot的函数
network_test.ipynb包含自己写的和助教提供的网络，可以生成相应文件
Play.ipynb用自己的agent进行一局游戏
test_class_clustering.ipynb包含该程序需要的所有函数，并且可以用来测试
train.ipynb用于训练

运行方法：
所有的.py文件只有evaluate.py是可执行文件，python3 evaluate.py执行
ipynb文件执行方式：
>>cd 路径
>>jupyter notebook 
打开相应文件运行即可

模型文件：
final.h5是该模型最终使用的文件，使用助教的网络和在线学习方法训练得到的模型
learn_32.h5,learn_128.h5,learn_128_512_train_online_inhabit.h5是运用模型分层策略和数据分层方法训练的模型，其中第一个和第三个建立在助教模型基础上经过修改得到的。
第二个是自己写的网络，可以在network_test.ipynb中查看。该模型并未达到高分，因为效果不好，中间终止训练。
模型文件链接：https://pan.baidu.com/s/1SaoCkuUCAGLOTtYfyKuWmQ