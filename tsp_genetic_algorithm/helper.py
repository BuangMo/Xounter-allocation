import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(distance, mean_distance):
    fig1 = plt.figure(1)
    ax1 = fig1.add_subplot(111)
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    ax1.set_title('Best Distance')
    ax1.set_xlabel('Number of Generations')
    ax1.set_ylabel('Distance')
    ax1.plot(distance)
    ax1.plot(mean_distance)
    plt.ylim(ymin=0)
    plt.text(len(distance)-1, distance[-1], str(distance[-1]))
    plt.text(len(mean_distance)-1, mean_distance[-1], str(mean_distance[-1]))
    plt.show()
    plt.pause(1)
    
def plot_fittest(coord):
    coord.append(coord[0])
    
    fig2 = plt.figure(2)
    ax2 = fig2.add_subplot(111)
    
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    ax2.set_title('Fittest Individual')
    plt.set_xlabel('X')
    plt.set_ylabel('Y')
    for i in range(1, len(coord)):
        tmp = coord[i-1]
        ax2.plot([coord[i][0], tmp[0]], [coord[i][1], tmp[1]], 'or-')
    plt.ylim(ymin=0)
    plt.show()
    plt.pause(1)