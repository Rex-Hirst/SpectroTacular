# SpectroTacular
This project uses a [short-time Fourier transform (STFT)](https://en.wikipedia.org/wiki/Short-time_Fourier_transform) to convert live audio input into a [spectrogram](https://en.wikipedia.org/wiki/Spectrogram).

$$\textbf{STFT}\{x(t)\}(τ,w) ≡ X(τ,w) = \int_{-\infty}^\infty x(t)w(t−τ)e^{-iwt} dt$$

The spectrogram is plotted using Matplotlib.
