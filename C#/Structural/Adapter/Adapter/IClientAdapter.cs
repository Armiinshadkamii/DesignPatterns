using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Adapter
{
    // 1- using an interface for the client, we keep the client
    // code away from changing. this means that we can add
    // new adapter classes without changin the client code.

    // An interface accept all types and implementations that 
    // implement it

    // 2- using interfaces the methods for all childs reamain the same

    // 3- if you are working in a team, everyone will know the signiture
    // of mehtods
    public interface IClientAdapter
    {
        string GetRequest();
    }
}
