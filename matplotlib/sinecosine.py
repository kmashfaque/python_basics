from matplotlib import pyplot as plt
import numpy as np

# t = np.arange(0, 4*np.pi, 0.5)
t = np.linspace(-np.pi, np.pi)


plt.plot(t, np.sin(t), antialiased=True)
plt.plot(t, np.cos(t), antialiased=True)
# plt.xticks(t)
plt.title("sine cosine graph")
plt.xlabel("angle")
plt.ylabel("sine cosine value")
plt.legend(["sin", "cos"])
plt.tight_layout()
plt.show()
