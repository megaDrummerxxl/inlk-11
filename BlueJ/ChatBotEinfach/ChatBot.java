public class ChatBot
{
    private Eingabeleser eingabe;

    public ChatBot()
    {
        eingabe = new Eingabeleser();
    }

    private void begruessung()
    {
        System.out.println("Hallo");
    }

    private void verabschiedung()
    {
        System.out.println("! Hallo");
    }

    public void start()
    {
        begruessung();

        while(true)
        {
            String in = eingabe.gibEingabe().toLowerCase();

            if(in.equals("ende") || in.equals("stop"))
            {
                verabschiedung();
                break;
            }else
            {
                System.out.println(Beantworter.gibAntwort(in));
            }
        }

    }
}
