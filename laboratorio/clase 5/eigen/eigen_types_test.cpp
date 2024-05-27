
#include <iostream>
#include <eigen3/Eigen/Dense>

using Eigen::MatrixXd;
using Eigen::VectorXd;

VectorXd matrix_vector_multiplication(const MatrixXd& matrix, const VectorXd& vector) {
    return matrix * vector;
}


int main() {
    // Example usage
    MatrixXd A(3, 3);
    A << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;

    VectorXd b(3);
    b << 1, 2, 3;

    VectorXd c = matrix_vector_multiplication(A, b);

    std::cout << "Result of matrix-vector multiplication: " << c.transpose() << std::endl;

    return 0;
}
