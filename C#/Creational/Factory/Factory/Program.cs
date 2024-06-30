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
            Creator chair = null;

            if(type == "Royal")
            {
                // Choose Factory
                chair = new RoyalCreator();
            }
            else if(type == "Modern")
            {
                chair = new ModernCreator();
            }
            // Create Object
            var product = chair.CreateObject();

            // Use the object
            Console.WriteLine(product.CreateChair());
  
            // some operation is now common among these objects.
            Console.WriteLine(chair.SomeOperation());
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
        return "Modernnnn Chair";
    }

}

class RoyalChair : IChair
{
    public string CreateChair()
    {
        return "Royallll Chair";
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
    public abstract IChair CreateObject();
    
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
    public override IChair CreateObject()
    {
        return new ModernChair();
    }
}

class RoyalCreator : Creator
{
    public override IChair CreateObject()
    {
        return new RoyalChair();
    }
}