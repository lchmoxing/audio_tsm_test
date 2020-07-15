#   使用deepspeech作为black-box ASR教程
## 服务器登录
ssh usslab@10.14.103.254
password: db2013
## 激活虚拟环境
cd qinhong/deepspeech
source deepspeech_env/bin/activate
## 进入python文件文件夹并运行测试python文件
cd ~/qinhong/deepspeech/DeepSpeech-0.7.1/DeepSpeech-0.7.1/native_client/python
python bayes_deepspeech.py --model ~/qinhong/deepspeech/deepspeech-0.7.1-models.pbmm --scorer ~/qinhong/deepspeech/deepspeech-0.7.1-models.scorer

bayes_deepspeech.py是运行的优化测验程序
##  使用注意事项
1、修改优化算法只需要修改bayes_deepspeech.py中black_box_function及后面程序，其余的不用修改。
2、使用时另外创建.py复制bayes_deepspeech.py的代码，不要直接在bayes_deepspeech.py中修改覆盖。
