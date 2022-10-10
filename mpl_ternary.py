# =========================================================================== #
#                                                                             #
#   These are the Python functions required for making ternary plots.         #
#                                                                             #
#   Copyright (c) 22022-present   Marco A. Lopez-Sanchez                      #
#                                                                             #
#   Licensed under the Apache License, Version 2.0 (the "License");           #
#   you may not use this file except in compliance with the License.          #
#   You may obtain a copy of the License at                                   #
#                                                                             #
#       http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                             #
#   Unless required by applicable law or agreed to in writing, software       #
#   distributed under the License is distributed on an "AS IS" BASIS,         #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#   See the License for the specific language governing permissions and       #
#   limitations under the "License".                                          #
#                                                                             #
#   Version 1.0                                                               #
#   For details see: https://github.com/marcoalopez/ternary_plots             #
#                                                                             #
# =========================================================================== #

import matplotlib.pyplot as plt
from types import SimpleNamespace


def tri2cartX(upper_apex, right_apex, left_apex):
    """ Converts ternary to Cartesian x coordinates."""
    return 0.5 * (upper_apex + 2 * right_apex) / (upper_apex + right_apex + left_apex)


def tri2cartY(upper_apex, right_apex, left_apex):
    """ Converts ternary to Cartesian y coordinates."""
    return (3**0.5 / 2) * upper_apex / (upper_apex + right_apex + left_apex)


def tri2cart(upper_apex, right_apex, left_apex):
    """ Converts ternary to Cartesian coordinates.
    Normalises input values and returns Cartesian
    coordinates x, y as a float or array.

    Parameters
    ----------
    upper_apex : numeric or array-like
        coordinate related to the upper corner/apex
    right_apex : numeric or array-like
        coordinate related to the right corner/apex
    left_apex : numeric or array-like
        coordinate related to the left corner/apex

    Example
    -------
    x, y = tri2cart(20, 10.5, 3.2)
    """

    # normalize
    total = upper_apex + right_apex + left_apex
    upper_apex = upper_apex / total
    right_apex = right_apex / total
    left_apex = left_apex / total

    return tri2cartX(upper_apex, right_apex, left_apex), tri2cartY(upper_apex, right_apex, left_apex)


def ternary(upper_label=None, left_label=None, right_label=None, **fig_kw):
    """ No-fuss ternary plot using matplotlib, meaning: A simple
    ternary diagram using matplolib with the minimum necessary
    elements. It requires no other dependencies than matplolib.
    Returns the figure and axe objects with which you can use the
    typical matplotlib functions such as plot(), scatter(), etc.
    Coordinates must be converted from ternary to Cartesian for use.
    See tri2cart() function.

    Parameters
    ----------
    upper_label : str, optional
        the label of the upper corner/apex
    right_label : str, optional
        the label of the right corner/apex
    left_label : str, optional
        the label of the left corner/apex
    """

    # set grid (each 0.2)
    slines = (
              # //CB
              SimpleNamespace(x1=tri2cartX(4/5, 0, 1/5), y1=tri2cartY(4/5, 0, 1/5),
                              x2=tri2cartX(4/5, 1/5, 0), y2=tri2cartY(4/5, 1/5, 0)),
              SimpleNamespace(x1=tri2cartX(3/5, 0, 2/5), y1=tri2cartY(3/5, 0, 2/5),
                              x2=tri2cartX(3/5, 2/5, 0), y2=tri2cartY(3/5, 2/5, 0)),
              SimpleNamespace(x1=tri2cartX(2/5, 0, 3/5), y1=tri2cartY(2/5, 0, 3/5),
                              x2=tri2cartX(2/5, 3/5, 0), y2=tri2cartY(2/5, 3/5, 0)),
              SimpleNamespace(x1=tri2cartX(1/5, 0, 4/5), y1=tri2cartY(1/5, 0, 4/5),
                              x2=tri2cartX(1/5, 4/5, 0), y2=tri2cartY(1/5, 4/5, 0)),
              # //AB
              SimpleNamespace(x1=tri2cartX(0, 1/5, 4/5), y1=tri2cartY(0, 1/5, 4/5),
                              x2=tri2cartX(1/5, 0, 4/5), y2=tri2cartY(1/5, 0, 4/5)),
              SimpleNamespace(x1=tri2cartX(0, 2/5, 3/5), y1=tri2cartY(0, 2/5, 3/5),
                              x2=tri2cartX(2/5, 0, 3/5), y2=tri2cartY(2/5, 0, 3/5)),
              SimpleNamespace(x1=tri2cartX(0, 3/5, 2/5), y1=tri2cartY(0, 3/5, 2/5),
                              x2=tri2cartX(3/5, 0, 2/5), y2=tri2cartY(3/5, 0, 2/5)),
              SimpleNamespace(x1=tri2cartX(0, 4/5, 1/5), y1=tri2cartY(0, 4/5, 1/5),
                              x2=tri2cartX(4/5, 0, 1/5), y2=tri2cartY(4/5, 0, 1/5)),
              # //AC
              SimpleNamespace(x1=tri2cartX(0, 4/5, 1/5), y1=tri2cartY(0, 4/5, 1/5),
                              x2=tri2cartX(1/5, 4/5, 0), y2=tri2cartY(1/5, 4/5, 0)),
              SimpleNamespace(x1=tri2cartX(0, 3/5, 2/5), y1=tri2cartY(0, 3/5, 2/5),
                              x2=tri2cartX(2/5, 3/5, 0), y2=tri2cartY(2/5, 3/5, 0)),
              SimpleNamespace(x1=tri2cartX(0, 2/5, 3/5), y1=tri2cartY(0, 2/5, 3/5),
                              x2=tri2cartX(3/5, 2/5, 0), y2=tri2cartY(3/5, 2/5, 0)),
              SimpleNamespace(x1=tri2cartX(0, 1/5, 4/5), y1=tri2cartY(0, 1/5, 4/5),
                              x2=tri2cartX(4/5, 1/5, 0), y2=tri2cartY(4/5, 1/5, 0))
              )

    # make plot
    fig, ax = plt.subplots(constrained_layout=True, **fig_kw)

    # draw master (triangle) lines
    ax.plot([0, 1], [0, 0], '-', color='black', linewidth=2, zorder=11)
    ax.plot([0, 0.5], [0, 0.8660254], '-', color='black', linewidth=2, zorder=11)
    ax.plot([0.5, 1], [0.8660254, 0], '-', color='black', linewidth=2, zorder=11)

    # draw grid lines
    for line in slines:
        ax.plot([line.x1, line.x2], [line.y1, line.y2], '-', color='grey', linewidth=1, zorder=1)

    if upper_label is not None:
        ax.text(x=0.5, y=0.91, s=upper_label, fontsize=14,
                horizontalalignment='center', verticalalignment='top', zorder=11)
        ax.text(x=1.05, y=-0.01, s=right_label, fontsize=14,
                horizontalalignment='center', verticalalignment='top', zorder=11)
        ax.text(x=-0.05, y=-0.01, s=left_label, fontsize=14,
                horizontalalignment='center', verticalalignment='top', zorder=11)

    # Prettify
    ax.set_axis_off()  # remove the box, ticks, etc.
    ax.axis('equal')  # ensure equal aspect ratio

    return fig, ax


if __name__ == '__main__':
    pass
else:
    print('no-fuss ternary plots imported')
