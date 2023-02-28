from os.path import isdir,isfile,islink,exists
from sys import argv,exit
class WordCounter:
    @staticmethod #sınıf,örneklemeye ihtiyaç duymayacağındann veya herhangi bir sınıf niteliği barındırmayacağından dolayı bu metodu yazdık
    def check_arguments(option):
        allowed_args="-l","w","c","--help"
        if option in allowed_args: #=>burada argüman kontrolünü yaptık
            return True
        else:
            return False

    def help_page(): #=>yardım sayfasını gösteren bir metot
        msg="""
        WordCounter Help Page --

        =>Word counter dosyalarınıza kaç satır,kelime veya karakter olduğunu gösteren,Python ile kodlanmış bir programdır.

        -- wdc [OPTION] [FILE]

        Examples:

        wdc -l example.txt
        wdc -w example.txt
        wdc -c example.txt
        wdc -l example.txt
        wdc example.txt

        -l:\t Dosyadaki satır sayısını göster
        -w:\t Dosyadaki kelime sayısını göster
        -c:\t Dosyadaki karakter sayısını göster


        =>Herhangi vir parametre kullanılmadığında tüm biilgiler gösterilir.
        
        """
        return msg
    

    @staticmethod
    def check_file(file):
        if not exists(file):
            return 4
        if isfile(file):
            return 1
        if isdir(file):
            return 2
        if islink(file):
            return 3

        
    @staticmethod
    def line_count(file=None,data=None): #=>metoda hem data hem de file şeklinde parametreler ekledik.
        if not data:
            #eğer ki verilmiş bir data yoksa:
            with open(file) as f:
                data=f.read()
        l=data.count("\n") + 1 #kaç satır başı olduğunu  bulduk
        if data[-1]=="\n":#eğer satır başı yapılmış lakin satıra bir şey yazılmamışsa
            l-=1
        return 1
    @staticmethod
    def word_count(file=None,data=None):
        if  not data:
            #Eğer ki verilmiş bir data yoksa
            with open(file) as f:
                data=f.read()
            data=data.replace("\n"," ")
            w=len(data.split(" "))
        return w
    @staticmethod
    def char_count(file=None,data=None):
        if not data:
            #eğerki verilmiş bir data yoksa
            with open(file) as f:
                data=f.read()
        c=len(data)
        return c
    def main():
        if len(argv)==2:
            #No Arguments
            file_or_argv=argv[-1]
            if file_or_argv=="--help":
                print(WordCounter.help_page())
                exit()
            if WordCounter.check_file(file_or_argv)==1:
                #Print all options
                with open (file_or_argv) as f:
                    data=f.read()
                result=f"{WordCounter.line_count(data=data)} {WordCounter.word_count(data=data)} {WordCounter.char_count(data=data)} :{file_or_argv}"

                print(result)
            elif WordCounter.check_file(file_or_argv)==2:
                print("Bu bir dizin!")
                exit()
            elif WordCounter.check_file(file_or_argv)==3:
                print("Bu bir link")
            else:
                print("Biçim tanınmıyor!")
                exit()
        elif len(argv)==3:
            #Have One Argument 
            file=argv[2]
            option=argv[1]
            if WordCounter.check_arguments(option) and WordCounter.check_file(file):
                if option=="-l":
                    result=f"{WordCounter.word_count(file=file)} {file}"
                    print(result)

                elif option=="-w":
                    result=f"{WordCounter.word_count(file=file)} {file}"
                    print(result)
                
                elif option=="-c":
                    result=f"{WordCounter.char_count(file=file)} {file}"
                    print(result)
               

                else:
                    print(WordCounter.help_page())
            else:
                print(WordCounter.help_page())
        else:
            print(WordCounter.help_page())




    if __name__=="__main__":
        main()
    else:
        pass
    




        











































































