

using Adapter;

class Program
{
    static void Main(String[] args)
    {
        // The program works with string data
        string data = null;

        // We wanna work with a common interface so that we keep 
        // the client code away from many changes.
        IClientAdapter clientAdaptor = null;

        // This is the incompatable interface
        Adaptee adaptee = new Adaptee();

        // Here we initialize an adapter. If we need to change the 
        // programs behavior and adapter we just change this 1 line
        // of code
        clientAdaptor = new Adaptor2(adaptee);
        //data = adaptee.SendData(); cant convert type int to string...

        data = clientAdaptor.GetRequest();
        Console.WriteLine(data);
    }
}

// The client cant use this class because
// it has incompatable interface. it returns
// int but the program needs string data.
class Adaptee
{
    public int SendData()
    {
        return 200;
    }
}

// Therefore we create an adaptor class
// and adapt the interfaces.
class Adaptor : IClientAdapter
{
    private readonly Adaptee _adaptee;
    public Adaptor(Adaptee adaptee)
    {
        _adaptee= adaptee;
    }

    public string GetRequest()
    {
        int intVal =  _adaptee.SendData();

        return intVal.ToString();

    }
}

class Adaptor2 : IClientAdapter
{
    private readonly Adaptee _adaptee;

    public Adaptor2(Adaptee adaptee)
    {
        _adaptee = adaptee;
    }

    public string GetRequest()
    {
        int Val = _adaptee.SendData();
        string ValStr = Val.ToString() + " ways";
        
        return ValStr;
    }
}