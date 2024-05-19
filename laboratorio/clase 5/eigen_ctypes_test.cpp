
#include <iostream>
#include <eigen3/Eigen/Dense>
#include <dlfcn.h>

using namespace Eigen;

extern "C" {
    void matrix_vector_multiply(double* matrix, double* vector, double* result, int rows, int cols) {
        Map<MatrixXd> mat(matrix, rows, cols);
        Map<VectorXd> vec(vector, cols);
        Map<VectorXd> res(result, rows);
        res = mat * vec ;
    }
}
