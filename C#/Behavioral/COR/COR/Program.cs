using COR;

class Program
{
    static void Main(string[] args)
    {
        IHandler handler = null;

        Login login = new Login();
        Pass pass = new Pass();
        Role role = new Role();

        login.SetNext(pass).SetNext(role);

        Console.WriteLine(login.Handle());
    }
}

class Login : IHandler
{
    private IHandler _nextHandler;

    public string Handle()
    {
        bool userExistance = true;
        if (userExistance)
        {
           return _nextHandler.Handle();
        }
        else
        {
            return "Access denied";
        }
    }

    public IHandler SetNext(IHandler nextHandler)
    {
        _nextHandler = nextHandler;

        return _nextHandler;
    }
}


class Pass : IHandler
{
    private IHandler _nextHandler;

    public string Handle()
    {
        bool userPass = true;
        if (userPass)
        {
            return _nextHandler.Handle();
        }
        else
        {
            return "Access denied";
        }
    }

    public IHandler SetNext(IHandler nextHandler)
    {
        _nextHandler = nextHandler;

        return _nextHandler;
    }
}

class Role : IHandler
{
    private IHandler _nextHandler;

    public string Handle()
    {
        bool usersRoleIsCustomer = true;
        if (usersRoleIsCustomer)
        {
            return "Ok";
        }
        else
        {
            return "Access denied";
        }
    }

    public IHandler SetNext(IHandler nextHandler)
    {
        _nextHandler = nextHandler;

        return _nextHandler;
    }
}