import matplotlib.pyplot as plt
import seaborn as sns

def set_styles():
    sns.set_style(style='whitegrid')
    sns.set_context("paper")
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['lines.linewidth'] = 1
    plt.rcParams['lines.markeredgewidth'] = 0
    plt.rcParams['lines.markersize'] = 8
    plt.rcParams['lines.markeredgecolor'] = (0, 0, 0, 0)
    SMALL_SIZE = 16
    MEDIUM_SIZE = 18
    BIGGER_SIZE = 20

    plt.rc('font', family='Helvetica')
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    
def read_palette(palette_file, mode='rgba'):
    color_dict = {}
    with open(palette_file, 'r') as open_file:
        if mode == 'rgba':
            for line in open_file.readlines():
                if line[0] == '$':
                    color_name = line.split(':')[0][1:]
                    rgba_str = line.split(': rgba')[1][1:-3]
                    rgb_values = rgba_str.split(', ')[:-1]
                    norm_rgb_values = [float(x)/255 for x in rgb_values]
                    color_dict[color_name] = norm_rgb_values
        elif mode == 'hex':
            for line in open_file.readlines():
                if line[0] == '$':
                    color_name = line.split(':')[0][1:]
                    hex_str = line.split(': ')[1].strip()
                    color_dict[color_name] = hex_str
    return color_dict
                

colors = read_palette('palettes-hex.scss', mode='hex')

sys_colors = {
    's':colors['color7'],
    'se':colors['color6'],
    'as':colors['color5'],
    'asn':colors['color4'],
    'p':colors['color3'],
    'pn':colors['color2'],
}

petal_styles = {
    '08':'-',
    '10':'--',
    '12':':'
}

def cm2inch(value):
    return value/2.54

def new_figure(height=5, type='body'):
    if type == 'body':
        width = 10.75
    elif type == 'margin':
        width = 5
    elif type == 'wide':
        width = 16.5
    else:
        width = 10.75
    fig, axes = plt.subplots(figsize=(width, height))
    fig.set_tight_layout(True)
    return fig, axes

def tuftefy(ax):
    if ax.legend != None:
        ax.legend(frameon=False) # remove legend outlines
    
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(True)
    ax.spines["bottom"].set_visible(True)
    #ax.spines["bottom"].set_color('grey')
    #ax.grid(color="w", alpha=0.5)
    ax.get_yaxis().grid(False)
    ax.get_xaxis().grid(False)
    ax.tick_params(axis='both', which='major', pad=0)
    ax.edgecolor = 1
    ax.edgewidth = 0.5
    
def save_figure(figure, name):
    figure.savefig('../images/{}'.format(name), dpi=600/2.54)