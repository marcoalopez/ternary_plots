# No-fuss ternary plots in Python

**What is a ternary plot?**  
A [ternary plot](https://en.wikipedia.org/wiki/Ternary_plot) is a triangular diagram that displays the proportion of three variables that sum to a constant, usually 1 or 100%. It is a common diagram in solid-earth sciences but is also used in other physical sciences.

**What is the purpose of this repository?**  
You want to use ternary diagrams in your Jupyter notebook (or script) while using Python. Sadly you realise that matplolib does not have ternary plots by default. After some research on the internet, you realise that the alternatives are either to install other plotting libraries (e.g. [Plotly](https://plotly.com/python/ternary-plots/)) or to install third-party libraries that rely on matplolib (e.g. [python-ternary](https://github.com/marcharper/python-ternary) or [mpltern](https://mpltern.readthedocs.io/en/latest/index.html)). Unfortunately, you don't feel like learning a new syntax for plotting (you are too comfortable with your matplolib buddy) or don't want to install a new Python library with all that this entails (dependencies, etc.) and that it seem too overkill for what you need\*. This is where the good news comes in. Matplotlib allows you to create a simple ternary diagram in very few lines of code, where simple means that it has the minimum necessary elements to correctly interpret a ternary diagram. In short, **no installations, no new dependencies, your usual matplolib syntax, and no fuss**.

\*_I have nothing against these libraries, quite the opposite, if you need to do more advanced things use them!_

**How to use it?**  
Simply copy and paste the functions into your Jupyter notebook cells and follow the usage examples. Alternatively, you can download the python file containing the functions and save it to the same folder where your notebook is located. Then simply run the script using ``%run ternary.py`` or import it as a module.



**Examples available soon!**



## License

[![Creative Commons Licence](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)
All the notebooks are licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

---

*Copyright © 2022 Marco A. Lopez-Sanchez*  

*Information presented on this website and the notebooks is provided without any express or implied warranty and may include technical inaccuracies or typing errors; the author reserve the right to modify or enhance the content of this website as well as the notebooks at any time without previous notice. This webpage and the notebooks are not liable for the content of external links. Notebook contents under [Creative Commons Attribution license CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) and codes under [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/).*

*Hosted on GitHub Pages*
