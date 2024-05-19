
#include <iostream>
#include <fstream>
#include <eigen3/Eigen/Dense>

using Eigen::MatrixXd;
using Eigen::VectorXd;

VectorXd matrix_vector_multiplication(const MatrixXd& matrix, const VectorXd& vector) {
    return matrix * vector;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " input_file output_file" << std::endl;
        return 1;  // codigo 1 para cantidad incorrecta de argumentos.
    }

    const char* input_file = argv[1];
    const char* output_file = argv[2];

    std::ifstream fin(input_file);
    if (!fin.is_open()) {
        std::cerr << "Error: could not open input file " << input_file << std::endl;
        return 1;
    }

    // Read matrix and vector from file
    int nrows, ncols;
    fin >> nrows >> ncols;

    MatrixXd A(nrows, ncols);
    for (int i = 0; i < nrows; i++) {
        for (int j = 0; j < ncols; j++) {
            fin >> A(i, j);
        }
    }

    VectorXd b(ncols);
    for (int i = 0; i < ncols; i++) {
        fin >> b(i);
    }

    fin.close();

    // Perform matrix-vector multiplication
    VectorXd c = matrix_vector_multiplication(A, b);

    // Write result to output file
    std::ofstream fout(output_file);
    if (!fout.is_open()) {
        std::cerr << "Error: could not open output file " << output_file << std::endl;
        return 1;
    }

    fout << c.transpose() << std::endl;

    fout.close();

    return 0;
}




