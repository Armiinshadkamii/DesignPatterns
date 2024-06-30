using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace COR
{
    public interface IHandler
    {
        IHandler SetNext(IHandler nextHandler);
        string Handle();
    }
}
