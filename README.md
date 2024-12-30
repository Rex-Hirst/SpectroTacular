# SpectroTacular
This project uses a [short-time Fourier transform (STFT)](https://en.wikipedia.org/wiki/Short-time_Fourier_transform) to convert live audio input into a [spectrogram](https://en.wikipedia.org/wiki/Spectrogram).

$$\textbf{STFT}\{x(t)\}(τ,w) ≡ X(τ,w) = \int_{-\infty}^\infty x(t)w(t−τ)e^{-iwt} dt$$

The ouput is plotted using Matplotlib, creating a moving spectrogram that looks like this:

![Figure_1](https://github.com/user-attachments/assets/22bc7f2d-0886-42e8-9894-e04446f2c9f7)
