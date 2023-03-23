import matplotlib.pyplot as plt
import pandas as pd
 
# 绘制轨迹
if __name__ == '__main__':
    
    fig, ax1 = plt.subplots(1, 1) 

    #设置上方和右方无框
    ax1.spines['top'].set_visible(False)                   # 不显示图表框的上边框
    ax1.spines['right'].set_visible(False)  
    name="traj"
    data = pd.read_csv("不好算法对应的里程位姿数据shuju2.csv")


  
 
    #设置折线颜色，折线标签
    #使用平滑处理
    ax1.plot(data['field.pose.pose.position.x'], data['field.pose.pose.position.y'], color="red",label='bad')

    #不使用平滑处理
    # ax1.plot(len_mean['Step'], len_mean['Value'], color="red",label='all_data')
 
 
    #s设置标签位置，lower upper left right，上下和左右组合
    fig.legend(loc = 'upper right')

    ax1.set_xlabel("x/m")
    ax1.set_ylabel("y/m")
    plt.show()
    #保存图片，也可以是其他格式，如pdf
    fig.savefig(fname='./'+name+'.png', format='png')
 
