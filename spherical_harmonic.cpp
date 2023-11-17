#include <cmath>
#include <algorithm>
#include <complex>
#include <iostream>

extern "C" {

double spherical_harmonic_real(double theta, double phi, int l, int m) {
    double Ylm = std::sqrt((2*l + 1) * (std::tgamma(l - std::abs(m) + 1)) / (4.0 * M_PI * std::tgamma(l + std::abs(m) + 1))) 
                          * std::cos(m * phi) * std::cos(m * theta);
    std::cout << Ylm << std::endl;
    if (m < 0){
        Ylm = std::pow(-1, m) * Ylm;
    }                     
    return Ylm;

}

double spherical_harmonic_imag(double theta, double phi, int l, int m) {
    double Ylm = std::sqrt((2*l + 1) * (std::tgamma(l - std::abs(m) + 1)) / (4.0 * M_PI * std::tgamma(l + std::abs(m) + 1))) 
                          * std::sin(m * phi) * std::cos(m * theta);
    if (m < 0){
        Ylm = std::pow(-1, m) * Ylm;
    }                     
    return Ylm;
}



}

