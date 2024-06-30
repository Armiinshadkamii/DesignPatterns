// See https://aka.ms/new-console-template for more information

using System.Net.NetworkInformation;
using System;
using System.IO;

// Using this factory approach to object creation, we 
// can easily change the type of object that the system
// is working with.
// Also object creation is centralized and the code is
// easier to maintain since everything is seprate and 
// these classes all have an abstraction or interface
// that they need to follow.


class Program
{
    static void Main(string[] args)
    {
        while (true)
        {
            Console.WriteLine("Type of chair:\n1-Modern\n2-Royal\n ");
            string type = Console.ReadLine();

            // Its is recommended to return objects to an object of type 
            // creator. this way returned concrete products have access 
            // to both their own signiture but also access to the signiture
            // of creator. because it has passed its signiture to concrete
            // creators through inheritance.
            Creator family = null;

            // Select a family
            if (type == "Royal")
            {
                family = new RoyalCreator();
            }
            else if (type == "Modern")
            {
                family = new ModernCreator();
            }

            // Create an object from that family
            ISofa Sofa = family.CreateSofaObject();
            // Use the object
            Console.WriteLine(Sofa.CreateSofa());

            // Create an object from that family
            IChair chair = family.CreateChairObject();
            // Use the object
            Console.WriteLine(chair.CreateChair());


            
        }
    }
} // Program

// This is the interface in which different implementations
// of chair product will be derived from 
interface IChair
{
    string CreateChair();
}

// Modern chair and Royal chair are different implementations
// of the Ichair interface
class ModernChair : IChair
{
    public string CreateChair()
    {
        return "Modern Chair";
    }
}

class RoyalChair : IChair
{
    public string CreateChair()
    {
        return "Royal Chair";
    }
}

interface ISofa
{
    string CreateSofa();
}

// Modern chair and Royal chair are different implementations
// of the Ichair interface
class ModernSofa : ISofa
{
    public string CreateSofa()
    {
        return "Modern Sofa";
    }
}

class RoyalSofa : ISofa
{
    public string CreateSofa()
    {
        return "Royal Sofa";
    }
}

// The creator class is the pattern in which all concrete creators 
// most follow. It is defined as abstract so that we can have both 
// mehtods that most be abstract and normal methods.
abstract class Creator
{
    // Since all chair products are drived from IChair interface
    // in order to not repeat create chair methods for each 
    // produt we just set the return type to be Ichair and it works.
    public abstract IChair CreateChairObject();
    public abstract ISofa CreateSofaObject();

    public string SomeOperation()
    {
        return "Some Operation";
    }
}

// Concrete creators return different implementations of 
// chair products
class ModernCreator : Creator
{
    // Note that this method doesnt necessarily need to 
    // return a modern chair. it can also return the type
    // of abc class it is derived from.
    public override IChair CreateChairObject()
    {
        return new ModernChair();
    }

    public override ISofa CreateSofaObject()
    {
        return new ModernSofa();
    }
}

class RoyalCreator : Creator
{
    public override IChair CreateChairObject()
    {
        return new RoyalChair();
    }

    public override ISofa CreateSofaObject()
    {
        return new RoyalSofa();
    }
}