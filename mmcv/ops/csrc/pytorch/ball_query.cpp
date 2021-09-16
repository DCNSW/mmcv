// Modified from
// https://github.com/sshaoshuai/Pointnet2.PyTorch/tree/master/pointnet2/src/ball_query.cpp

#include "pytorch_cpp_helper.hpp"

#ifdef MMCV_WITH_CUDA
void BallQueryForwardCUDAKerenlLauncher(int b, int n, int m, float min_radius,
                                        float max_radius, int nsample,
                                        const Tensor new_xyz, const Tensor xyz,
                                        int *idx);

void ball_query_forward_cuda(int b, int n, int m, float min_radius,
                             float max_radius, int nsample, Tensor new_xyz,
                             Tensor xyz, int *idx) {
  BallQueryForwardCUDAKerenlLauncher(b, n, m, min_radius, max_radius, nsample,
                                     new_xyz, xyz, idx);
};
#endif

void ball_query_forward(int b, int n, int m, float min_radius, float max_radius,
                        int nsample, at::Tensor new_xyz_tensor,
                        at::Tensor xyz_tensor, at::Tensor idx_tensor) {
  if (new_xyz_tensor.device().is_cuda()) {
#ifdef MMCV_WITH_CUDA
    CHECK_CUDA_INPUT(new_xyz_tensor);
    CHECK_CUDA_INPUT(xyz_tensor);
    int *idx = idx_tensor.data_ptr<int>();

    ball_query_forward_cuda(b, n, m, min_radius, max_radius, nsample,
                            new_xyz_tensor, xyz_tensor, idx);
#else
    AT_ERROR("ball_query is not compiled with GPU support");
#endif
  } else {
    AT_ERROR("ball_query is not implemented on CPU");
  }
}
