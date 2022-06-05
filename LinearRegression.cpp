#include <iostream>
#include <cmath>
using namespace std;
int main()
{
int a = 0, c = 2, m = 3, n = 2;
const int N = 100;
double x[N]{}, y[N]{};
double delta_x = (static_cast<double>(c) - a) / N;
for (int i = 0; i < N; i++)
{
x[i] = i * delta_x;
}
for (int i = 0; i < N; i++)
{
y[i] = 7 + m * cos(n * x[i]);
}
double sumOfx = 0;
double sumOfy = 0;
double sumOfxy = 0;
double sumOfxx = 0;
for (int i = 0; i < N; i++)
{
sumOfx = sumOfx + x[i];
}
for (int i = 0; i < N; i++)
{
sumOfy = sumOfy + y[i];
}
for (int i = 0; i < N; i++)
{
sumOfxy = sumOfxy + x[i]*y[i];
}
for (int i = 0; i < N; i++)
{
sumOfxx = sumOfxx + x[i] * x[i];
}
cout << "sumOfx: " << sumOfx << endl;
cout << "sumOfy: " << sumOfy << endl;
cout << "sumOfxy: " << sumOfxy << endl;
cout << "sumOfxx: " << sumOfxx << endl << endl;
 double k = 0.0, b = 0.0;
k = (N * sumOfxy - sumOfx * sumOfy) / (N * sumOfxx - sumOfx * sumOfx);
b = (sumOfy / N) - k * (sumOfx / N);
cout << "n: " << n << endl;
cout << "m: " << m << endl;
cout << "N: " << N << endl;
cout << "k: " << k << endl;
cout << "b: " << b << endl;
return 0;
}