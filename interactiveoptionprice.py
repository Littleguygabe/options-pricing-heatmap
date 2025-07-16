
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox, RadioButtons
import black_scholes

fig, ax = plt.subplots(figsize=(10, 10))
fig.subplots_adjust(right=0.85, bottom=0.3)
cbar_ax = fig.add_axes([0.88, 0.3, 0.03, 0.6])

ax_spotUpperSlider = fig.add_axes([0.25, 0.2, 0.65, 0.03])
ax_spotLowerSlider = fig.add_axes([0.25, 0.175, 0.65, 0.03])
ax_vUpperSlider = fig.add_axes([0.25, 0.15, 0.65, 0.03])
ax_vLowerSlider = fig.add_axes([0.25, 0.125, 0.65, 0.03])

# TextBox axes
ax_s_textbox = fig.add_axes([0.2, 0.07, 0.15, 0.04])
ax_k_textbox = fig.add_axes([0.5, 0.07, 0.15, 0.04])
ax_t_textbox = fig.add_axes([0.8, 0.07, 0.15, 0.04])
ax_sd_textbox = fig.add_axes([0.2, 0.01, 0.15, 0.04])
ax_r_textbox = fig.add_axes([0.5, 0.01, 0.15, 0.04])
rax = fig.add_axes([0.8,0.01,0.15,0.04])

# --- Initial Parameters ---
S = 100.0
K = 100.0
T = 1.0
R = 0.05
sd = 0.2
boundsMaxSize = 0.5


spotUpperSlider = Slider(ax=ax_spotUpperSlider, label='Spot Upper Δ', valmin=1, valmax=S*boundsMaxSize, valstep=1, valinit=S*0.5*boundsMaxSize)
spotLowerSlider = Slider(ax=ax_spotLowerSlider, label='Spot Lower Δ', valmin=(-S*boundsMaxSize)+1, valmax=0, valstep=1, valinit=-(S*0.5*boundsMaxSize))
vUpperSlider = Slider(ax=ax_vUpperSlider, label='Vol Upper Δ', valmin=0.005, valmax=sd*boundsMaxSize, valstep=0.005, valinit=sd*0.5*boundsMaxSize)
vLowerSlider = Slider(ax=ax_vLowerSlider, label='Vol Lower Δ', valmin=(-sd*boundsMaxSize)+0.01, valmax=-0.005, valstep=0.005, valinit=-(sd*0.5*boundsMaxSize))

s_textbox = TextBox(ax_s_textbox, "Base Spot (S)", initial=str(S))
k_textbox = TextBox(ax_k_textbox, "Strike (K)", initial=str(K))
t_textbox = TextBox(ax_t_textbox, "Time (T)", initial=str(T))
sd_textbox = TextBox(ax_sd_textbox, "Base Vol (sd)", initial=str(sd))
r_textbox = TextBox(ax_r_textbox, "Rate (R)", initial=str(R))

radio = RadioButtons(rax,['Call','Put'],active=0)


def update(val):
    ax.cla()
    spotLowerLimit = spotLowerSlider.val
    spotUpperLimit = spotUpperSlider.val
    sdLowerLimit = vLowerSlider.val
    sdUpperLimit = vUpperSlider.val

    sdRange = np.arange(max(sd + sdLowerLimit, 0.01), sd + sdUpperLimit, (sdUpperLimit - sdLowerLimit) / 10)
    spotRange = np.arange(S + spotLowerLimit, S + spotUpperLimit, (spotUpperLimit - spotLowerLimit) / 10)

    optionType = radio.value_selected

    data = []
    for curSd in sdRange:
        temparr = []
        for curSpot in spotRange:
            if optionType == 'Call':
                valOption = black_scholes.call(curSpot, K, T, R, curSd)

            else:
                valOption = black_scholes.put(curSpot, K, T, R, curSd) 

            temparr.append(round(valOption, 3))
        data.append(temparr)

    sns.heatmap(data, ax=ax, cmap='viridis', cbar=True, cbar_ax=cbar_ax, annot=True, fmt='.3f',
                xticklabels=sdRange.round(3), yticklabels=spotRange.round(3))
    ax.set_xlabel('Volatility (%)')
    ax.set_ylabel('Spot Price (£)')
    ax.set_title(f'{optionType} price heatmap')
    fig.canvas.draw_idle()

def submit_s(text):
    global S
    try:
        S = float(text)
        spotUpperSlider.valmax = S * boundsMaxSize
        spotUpperSlider.ax.set_xlim(1, S * boundsMaxSize)
        spotLowerSlider.valmin = (-S * boundsMaxSize) + 1
        spotLowerSlider.ax.set_xlim((-S * boundsMaxSize) + 1, 0)
        spotUpperSlider.set_val(S * 0.5 * boundsMaxSize)
        spotLowerSlider.set_val(-(S * 0.5 * boundsMaxSize))
        update(None)
    except ValueError:
        print(f"Invalid input for S: '{text}'. Please enter a number.")

def submit_sd(text):
    global sd
    try:
        sd = float(text)
        vUpperSlider.valmax = sd * boundsMaxSize
        vUpperSlider.ax.set_xlim(0.005, sd * boundsMaxSize)
        vLowerSlider.valmin = (-sd * boundsMaxSize) + 0.01
        vLowerSlider.ax.set_xlim((-sd * boundsMaxSize) + 0.01, -0.005)
        vUpperSlider.set_val(sd * 0.5 * boundsMaxSize)
        vLowerSlider.set_val(-(sd * 0.5 * boundsMaxSize))
        update(None)
    except ValueError:
        print(f"Invalid input for sd: '{text}'. Please enter a number.")

def submit_k(text):
    global K
    try:
        K = float(text)
        update(None)
    except ValueError:
        print(f"Invalid input for K: '{text}'. Please enter a number.")

def submit_t(text):
    global T
    try:
        T = float(text)
        update(None)
    except ValueError:
        print(f"Invalid input for T: '{text}'. Please enter a number.")

def submit_r(text):
    global R
    try:
        R = float(text)
        update(None)
    except ValueError:
        print(f"Invalid input for R: '{text}'. Please enter a number.")

# --- Event Handling ---
spotUpperSlider.on_changed(update)
spotLowerSlider.on_changed(update)
vUpperSlider.on_changed(update)
vLowerSlider.on_changed(update)
s_textbox.on_submit(submit_s)
sd_textbox.on_submit(submit_sd)
k_textbox.on_submit(submit_k)
t_textbox.on_submit(submit_t)
r_textbox.on_submit(submit_r)
radio.on_clicked(update)

# --- Initial Plot ---
update(None)
plt.show()
