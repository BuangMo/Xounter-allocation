import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(distance, mean_distance):
    fig1 = plt.figure(1)
    fig1.add_subplot(111)
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Best Distance')
    plt.ylabel('Number of Generations')
    plt.ylabel('Distance')
    plt.plot(distance)
    plt.plot(mean_distance)
    plt.ylim(ymin=0)
    plt.text(len(distance)-1, distance[-1], str(distance[-1]))
    plt.text(len(mean_distance)-1, mean_distance[-1], str(mean_distance[-1]))
    plt.show(block=False)
    plt.pause(1)
    
def plot_fittest(coord, original_set):
    coord.append(coord[0])
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    plt.figure(2)
    
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Fittest Individual')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    for i in range(len(original_set)):
        x = original_set[i][0]
        y = original_set[i][1]
        plt.annotate(labels[i], (x, y))
    
    for i in range(1, len(coord)):
        tmp = coord[i-1]
        x = [coord[i][0], tmp[0]]
        y = [coord[i][1], tmp[1]]
        plt.plot(x, y, 'or-')
        
    plt.ylim(ymin=0)
    plt.show(block=False)