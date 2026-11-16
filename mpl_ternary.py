# =========================================================================== #
#                                                                             #
#   These are the Python functions required for making ternary plots.         #
#                                                                             #
#   Copyright (c) 2022-present   Marco A. Lopez-Sanchez                      #
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


def make_grid(step=0.2):
    """ Generates the grid lines of a ternary diagram for a
    given step size. Returns a tuple of objects, each with the
    Cartesian coordinates (x1, y1) and (x2, y2) of the endpoints
    of a grid line.

    Parameters
    ----------
    step : float, optional
        the grid step size, a value between 0 and 1 that divides
        the axes evenly (e.g. 0.1, 0.2, 0.25). Default is 0.2.
    """

    n = round(1 / step)

    if n < 2 or abs(1 / step - n) > 1e-9:
        raise ValueError('step must be a value between 0 and 0.5 that divides 1 evenly (e.g. 0.1, 0.2, 0.25)')

    slines = []

    for i in range(1, n):
        f = i / n
        # //CB
        slines.append(SimpleNamespace(x1=tri2cartX(f, 0, 1 - f), y1=tri2cartY(f, 0, 1 - f),
                                      x2=tri2cartX(f, 1 - f, 0), y2=tri2cartY(f, 1 - f, 0)))
        # //AB
        slines.append(SimpleNamespace(x1=tri2cartX(0, f, 1 - f), y1=tri2cartY(0, f, 1 - f),
                                      x2=tri2cartX(f, 0, 1 - f), y2=tri2cartY(f, 0, 1 - f)))
        # //AC
        slines.append(SimpleNamespace(x1=tri2cartX(0, 1 - f, f), y1=tri2cartY(0, 1 - f, f),
                                      x2=tri2cartX(f, 1 - f, 0), y2=tri2cartY(f, 1 - f, 0)))

    return tuple(slines)


def make_labels(step=0.2):
    """ Generates the axis tick labels of a ternary diagram for a
    given grid step size. Returns a tuple of objects, each with
    the Cartesian coordinates (x, y), the text, and the horizontal
    (ha) and vertical (va) alignments of a tick label. Values are
    placed where the grid lines meet the edges: upper apex values
    along the left edge, right apex values along the right edge,
    and left apex values along the bottom edge.

    Parameters
    ----------
    step : float, optional
        the grid step size, a value between 0 and 1 that divides
        the axes evenly (e.g. 0.1, 0.2, 0.25). Default is 0.2.
    """

    n = round(1 / step)

    if n < 2 or abs(1 / step - n) > 1e-9:
        raise ValueError('step must be a value between 0 and 0.5 that divides 1 evenly (e.g. 0.1, 0.2, 0.25)')

    labels = []

    for i in range(1, n):
        f = i / n
        text = f'{f:.2g}'
        # left edge: upper apex values, increasing towards the upper apex
        labels.append(SimpleNamespace(x=tri2cartX(f, 0, 1 - f) - 0.02, y=tri2cartY(f, 0, 1 - f),
                                      text=text, ha='right', va='center'))
        # right edge: right apex values, increasing towards the right apex
        labels.append(SimpleNamespace(x=tri2cartX(1 - f, f, 0) + 0.02, y=tri2cartY(1 - f, f, 0),
                                      text=text, ha='left', va='center'))
        # bottom edge: left apex values, increasing towards the left apex
        labels.append(SimpleNamespace(x=tri2cartX(0, 1 - f, f), y=-0.02,
                                      text=text, ha='center', va='top'))

    return tuple(labels)


def ternary(upper_label=None, left_label=None, right_label=None, grid_step=0.2, tick_labels=True, **fig_kw):
    """ No-fuss ternary plot using matplotlib, meaning: A simple
    ternary diagram using Matplotlib with the minimum necessary
    elements. It requires no other dependencies than Matplotlib.
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
    grid_step : float, optional
        the grid step size, a value between 0 and 1 that divides
        the axes evenly (e.g. 0.1, 0.2, 0.25). Default is 0.2.
    tick_labels : bool, optional
        if True, draw the axis tick labels that fit the chosen
        grid. Default is True.
    """

    # set grid
    slines = make_grid(step=grid_step)

    # make plot
    fig, ax = plt.subplots(constrained_layout=True, **fig_kw)

    # draw master (triangle) lines
    ax.plot([0, 1], [0, 0], '-', color='black', linewidth=2, zorder=11)
    ax.plot([0, 0.5], [0, 0.8660254], '-', color='black', linewidth=2, zorder=11)
    ax.plot([0.5, 1], [0.8660254, 0], '-', color='black', linewidth=2, zorder=11)

    # draw grid lines
    for line in slines:
        ax.plot([line.x1, line.x2], [line.y1, line.y2], '-', color='grey', linewidth=1, zorder=1)

    # draw axis tick labels
    if tick_labels:
        for label in make_labels(step=grid_step):
            ax.text(x=label.x, y=label.y, s=label.text, fontsize=10, color='grey',
                    horizontalalignment=label.ha, verticalalignment=label.va, zorder=11)

    if upper_label is not None:
        ax.text(x=0.5, y=0.91, s=upper_label, fontsize=14,
                horizontalalignment='center', verticalalignment='top', zorder=11)
        ax.text(x=1.05, y=-0.01, s=right_label, fontsize=14,
                horizontalalignment='center', verticalalignment='top', zorder=11)
        ax.text(x=-0.05, y=-0.01, s=left_label, fontsize=14,
                horizontalalignment='center', verticalalignment='top', zorder=11)

    # Prettify
    ax.set_axis_off()  # remove the box, ticks, etc.
    ax.axis('equal')   # ensure equal aspect ratio

    return fig, ax


if __name__ == '__main__':
    pass
else:
    print('no-fuss ternary plots imported')
