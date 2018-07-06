using System;
using System.Collections.Generic;
using System.IO;

namespace CleanData
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] myMonth = new string[12] { "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12" };
            string name = "";
            for ( int m=0; m<12; m++ )
            {
                for( int d=1; d<32; d++ )
                {
                    if( d<10)
                        name = "2018_" + myMonth[m] + "_0" + d;
                    else
                        name = "2018_" + myMonth[m] + "_" + d;

                    LoadData(name);
                }
            }
            Console.WriteLine("Hello World!");
            Console.ReadLine();
        }

        static bool LoadData( string name )
        {
            string filePath = @"C:\Users\albert_shen\Desktop\historyData\2018\Raw\Daily_" + name + ".csv";
            if (!File.Exists(filePath))
            {
                Console.WriteLine(name + "does not exist!");
                return false;
            }

            StreamReader file = new StreamReader(filePath);
            int counter = 0;
            int cleanCount = 0;
            string line;
            List<string> listA = new List<string>();
            List<string> listB = new List<string>();
            List<string> listC = new List<string>();
            List<string> listD = new List<string>();
            List<string> listE = new List<string>();
            List<string> listF = new List<string>();

            while ((line = file.ReadLine()) != null)
            {
                string[] values = line.Split(',');
                if ( values.Length >= 6 && values[1].Trim() == "TX")
                {
                    listA.Add(values[0].Trim());    //--- Date
                    listB.Add(values[1].Trim());    //--- TX
                    listC.Add(values[2].Trim());    //--- month
                    listD.Add(values[3].Trim());    //--- hr,min,sec
                    listE.Add(values[4].Trim());    //--- Point
                    listF.Add(values[5].Trim());    //--- Volume
                    //Console.WriteLine(listA[cleanCount] + "/" + listB[cleanCount] + "/" + listC[cleanCount] + "/" + 
                    //                  listD[cleanCount] + "/" + listE[cleanCount] + "/" + listF[cleanCount] );
                    cleanCount++;
                }
                counter++;
            }

            //--- Save Data
            /*
            var csv = new System.Text.StringBuilder();
            for ( int i=0; i<cleanCount; i++ )
            {
                var newLine = $"{listA[i]},{listB[i]},{listC[i]},{listD[i]},{listE[i]},{listF[i]}";
                csv.AppendLine(newLine);
            }
            File.WriteAllText(@"C:\Users\albert_shen\Desktop\AAA.csv", csv.ToString());
            */


            file.Close();
            Console.WriteLine("There were {0} lines.", counter);
            Console.WriteLine("There were {0} clean lines.", cleanCount);
            return true;
        }
    }
}
