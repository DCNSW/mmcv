import pytest
import torch

from mmcv.ops import grouping_operation


def test_grouping_points():
    if not torch.cuda.is_available():
        pytest.skip()
    idx = torch.tensor([[[0, 0, 0], [3, 3, 3], [8, 8, 8], [0, 0, 0], [0, 0, 0],
                         [0, 0, 0]],
                        [[0, 0, 0], [6, 6, 6], [9, 9, 9], [0, 0, 0], [0, 0, 0],
                         [0, 0, 0]]]).int().cuda()
    festures = torch.tensor([[[
        0.5798, -0.7981, -0.9280, -1.3311, 1.3687, 0.9277, -0.4164, -1.8274,
        0.9268, 0.8414
    ],
                              [
                                  5.4247, 1.5113, 2.3944, 1.4740, 5.0300,
                                  5.1030, 1.9360, 2.1939, 2.1581, 3.4666
                              ],
                              [
                                  -1.6266, -1.0281, -1.0393, -1.6931, -1.3982,
                                  -0.5732, -1.0830, -1.7561, -1.6786, -1.6967
                              ]],
                             [[
                                 -0.0380, -0.1880, -1.5724, 0.6905, -0.3190,
                                 0.7798, -0.3693, -0.9457, -0.2942, -1.8527
                             ],
                              [
                                  1.1773, 1.5009, 2.6399, 5.9242, 1.0962,
                                  2.7346, 6.0865, 1.5555, 4.3303, 2.8229
                              ],
                              [
                                  -0.6646, -0.6870, -0.1125, -0.2224, -0.3445,
                                  -1.4049, 0.4990, -0.7037, -0.9924, 0.0386
                              ]]]).cuda()

    output = grouping_operation(festures, idx)
    expected_output = torch.tensor([[[[0.5798, 0.5798, 0.5798],
                                      [-1.3311, -1.3311, -1.3311],
                                      [0.9268, 0.9268, 0.9268],
                                      [0.5798, 0.5798, 0.5798],
                                      [0.5798, 0.5798, 0.5798],
                                      [0.5798, 0.5798, 0.5798]],
                                     [[5.4247, 5.4247, 5.4247],
                                      [1.4740, 1.4740, 1.4740],
                                      [2.1581, 2.1581, 2.1581],
                                      [5.4247, 5.4247, 5.4247],
                                      [5.4247, 5.4247, 5.4247],
                                      [5.4247, 5.4247, 5.4247]],
                                     [[-1.6266, -1.6266, -1.6266],
                                      [-1.6931, -1.6931, -1.6931],
                                      [-1.6786, -1.6786, -1.6786],
                                      [-1.6266, -1.6266, -1.6266],
                                      [-1.6266, -1.6266, -1.6266],
                                      [-1.6266, -1.6266, -1.6266]]],
                                    [[[-0.0380, -0.0380, -0.0380],
                                      [-0.3693, -0.3693, -0.3693],
                                      [-1.8527, -1.8527, -1.8527],
                                      [-0.0380, -0.0380, -0.0380],
                                      [-0.0380, -0.0380, -0.0380],
                                      [-0.0380, -0.0380, -0.0380]],
                                     [[1.1773, 1.1773, 1.1773],
                                      [6.0865, 6.0865, 6.0865],
                                      [2.8229, 2.8229, 2.8229],
                                      [1.1773, 1.1773, 1.1773],
                                      [1.1773, 1.1773, 1.1773],
                                      [1.1773, 1.1773, 1.1773]],
                                     [[-0.6646, -0.6646, -0.6646],
                                      [0.4990, 0.4990, 0.4990],
                                      [0.0386, 0.0386, 0.0386],
                                      [-0.6646, -0.6646, -0.6646],
                                      [-0.6646, -0.6646, -0.6646],
                                      [-0.6646, -0.6646, -0.6646]]]]).cuda()
    assert torch.allclose(output, expected_output)
