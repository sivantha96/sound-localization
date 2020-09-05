from matplotlib import pyplot as plt

# the function to plot the loss of the training process
def plot_history(history):
    hist_dict = history.history
    loss_reg = hist_dict['loss']
    plt.figure()
    plt.plot(loss_reg, 'b')
    plt.legend(['Training'])
    plt.ylabel("Training loss")
    plt.xlabel("Epoch")
    plt.draw()
    plt.show()
