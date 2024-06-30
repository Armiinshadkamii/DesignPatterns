

using Strategy;

class Program
{
    static void Main(string[] args)
    {
        Strategy1 strategy1 = new Strategy1();
        Strategy2 strategy2= new Strategy2();

        Context context = new Context(strategy2);
        Console.WriteLine(context.Execute());
    }
}

class Context
{
    private IStrategy _strategy;

    public Context() { }

    public Context(IStrategy strategy)
    {
        _strategy = strategy;
    }

    public void SetStrategy(IStrategy strategy)
    {
        _strategy = strategy;
    }

    public string Execute()
    {
        return _strategy.Do();
    }
}

class Strategy1 : IStrategy
{
    public string Do()
    {
        return "strategy 1 !";
    }
}

class Strategy2 : IStrategy
{
    public string Do()
    {
        return "strategy 2 !";
    }
}