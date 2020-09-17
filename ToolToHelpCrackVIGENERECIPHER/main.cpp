#include <iostream>
#include <fstream>
using namespace std;


int main()
{
    int dist=0;
    ifstream crytext("cipher.txt");
    char data[837];
    int n;

   cout <<"Letters     "<<"     Start   "<<"    End     "<<"Distance    "<<"Factors"<<endl;

    for(int x=0;x<837;x++)
    {
        crytext>>data[x];

    }

    for(int y=12;y<837;y++)
    {

    for(int w=0;w<837;w++)
    {
        if(w==y)
            break;
        if(w>y)
            break;

            if(data[w]==data[y])
            {
                if(data[w+1]==data[y+1])
                {
                    if(data[w+2]==data[y+2])
                    {
                        if(data[w+3]==data[y+3])
                        {
                            if(data[w+4]==data[y+4])
                            {
                    if((y-w)==dist)
                        break;
                    int afterw=4;
                    for(int c=5;c<100;c++)
                    {
                        if(data[w+c]==data[y+c])
                        {
                            afterw +=1;
                        }
                        else
                        {
                            for(int p=0;p<=afterw;p++)
                            {
                                cout<<data[w+p];
                            }
                            break;
                        }
                    }

                    n=(y-w);
                    dist=n;
                    cout<<"           "<<w<<"       "<<y<<"          "<<n<<"       "<<endl;

                    }
                }

            }
    }

    }
    }
    }

    return 0;
}

