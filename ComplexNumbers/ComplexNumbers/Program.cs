using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ComplexNumbers
{
    class Complex
    {
        public double real = 0.0;
        public double imaginary = 0.0;

        bool hasRealComponent;
        bool hasImaginaryComponent;

        public Complex(double r)
        {
            real = r;
            if (r != 0.0) { hasRealComponent = true; }
            else { hasRealComponent = false; }
            hasImaginaryComponent = false;
        }
        public Complex(double r, double img)
        {
            real = r;
            imaginary = img;
            if (r != 0.0) { hasRealComponent = true; }
            else { hasRealComponent = false; }

            if (img != 0.0) { hasImaginaryComponent = true; }
            else { hasImaginaryComponent = false; }
        }

        public static Complex operator+( Complex one, Complex two)
        {
            return new Complex(one.real + two.real, one.imaginary + two.imaginary);
        }
        public static Complex operator-(Complex one, Complex two)
        {
            return new Complex(one.real - two.real, one.imaginary - two.imaginary);
        }
        public static Complex operator*(Complex one, Complex two)
        {
            double r1, r2, r3, r4;
            r1 = one.real * two.real;
            r2 = one.imaginary * two.real;
            r3 = one.real * two.imaginary;
            r4 = one.imaginary * two.imaginary * (-1);
            return new Complex(one.real - two.real, one.imaginary - two.imaginary);
        }
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            if (hasRealComponent)
            {
                sb.Append(real.ToString());
            }
            if (hasImaginaryComponent)
            {
                if (imaginary > 0 && hasRealComponent) { sb.Append("+"); }

                if (imaginary == -1) { sb.Append("-"); }
                else if (imaginary == 1) { }
                else { sb.Append(imaginary.ToString()); }
                
                sb.Append("i");
            }
            if (!hasRealComponent && !hasImaginaryComponent)
            {
                sb.Append("0");
            }
            return sb.ToString();
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.Out.WriteLine(new Complex(4));
            Console.Out.WriteLine(new Complex(4,1));
            Console.Out.WriteLine(new Complex(-1, 6));
            Console.Out.WriteLine(new Complex(-2, -17));
            Console.Out.WriteLine(new Complex(-11.2, 21.4));
            Console.Out.WriteLine(new Complex(0, 21.4));
            Console.Out.WriteLine(new Complex(0));
            Console.Out.WriteLine(new Complex(13, 0));
            Console.Out.WriteLine(new Complex(1, -1));

            Console.Out.WriteLine(new Complex(1, -1) + new Complex(4, 1));
            Console.Out.WriteLine(new Complex(1, -1) - new Complex(3, -2));
        }
    }
}
