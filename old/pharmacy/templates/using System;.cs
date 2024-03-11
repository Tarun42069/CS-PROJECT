using System;
class Program
{
    static void Main()
    {
        // Taking inputs
        Console.Write("Enter age: ");
        int age = int.Parse(Console.ReadLine());

        Console.Write("Enter gender (male/female): ");
        string gender = Console.ReadLine().ToLower();

        Console.Write("Enter taxable income: ");
        double taxableIncome = double.Parse(Console.ReadLine());

        // Calculate and display income tax
        CalculateIncomeTax(age, gender, taxableIncome);
    }

    static void CalculateIncomeTax(int age, string gender, double taxableIncome)
    {
        if (age > 65 || gender == "female")
        {
            Console.WriteLine("Wrong category");
        }
        else if (age <= 65 && gender == "male")
        {
            double incomeTax = 0;

            if (taxableIncome <= 160000)
            {
                incomeTax = 0;
            }
            else if (taxableIncome <= 500000)
            {
                incomeTax = (taxableIncome - 160000) * 0.10;
            }
            else if (taxableIncome <= 800000)
            {
                incomeTax = (taxableIncome - 500000) * 0.20 + 34000;
            }
            else
            {
                incomeTax = (taxableIncome - 800000) * 0.30 + 94000;
            }

            Console.WriteLine($"Income Tax payable: {incomeTax}");
        }
        else
        {
            Console.WriteLine("Invalid gender input");
        }
    }
}
