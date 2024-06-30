

class Program
{
    static void Main(string[] args)
    {
        // Instead of writing all of this code for
        // achieving one task, we create a facade
        // which contains this complexity and we
        // hide the complexity from the user.
      
        //BuyFoodItems buyFood = new BuyFoodItems();
        //Console.WriteLine(buyFood.Buy("Pizza"));

        //Chef chef = new Chef();
       //Console.WriteLine(chef.Cook("Pizza"));

        //DesignCustomersPlate design = new DesignCustomersPlate();
        //Console.WriteLine(design.Design());

        //***************************************************************

        Facade facade = new Facade();
        Console.WriteLine(facade.Order("Pizza"));
    }
}

class Facade
{
    public string Order(string name)
    {
        BuyFoodItems buy = new BuyFoodItems();
        Chef chef = new Chef();
        DesignCustomersPlate design = new DesignCustomersPlate();

        Console.WriteLine(buy.Buy(name));
        Console.WriteLine(chef.Cook(name));
        Console.WriteLine(design.Design());
        return $"{name} is ready";
    }
}

class DesignCustomersPlate
{
    public string Design()
    {
        return "Design is ready";
    }
}


class Chef
{
    public string Cook(string foodsName)
    {
        return $"{foodsName} is ready";
    }
}

class BuyFoodItems
{
    public string Buy(string name)
    {
        return $"Food items for {name} are ready";
    }
}
