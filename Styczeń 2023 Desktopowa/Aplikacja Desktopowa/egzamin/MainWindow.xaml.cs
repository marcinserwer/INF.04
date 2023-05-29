using System; //https://github.com/dariusz-grubba
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace egzamin
{
    public partial class MainWindow : Window
    {

        const string maleLitery = "qwertyuiopasdfghjklzxcvbnm";
        const string duzeLitery = "QWERTYUIOPASDFGHJKLZXCVBNM";
        const string cyfry = "1234567890";
        const string znakiSpecjalne = @"~!@#$%^&*()+=-";

        public MainWindow()
        {
            InitializeComponent();
        }
        public string GenerujHaslo(bool czyMalaDuzaLitera, bool czyCyfry, bool czyZnakiSpecjalne, int length)
        {
            char[] haslo = new char[length];
            string charSet = "";
            System.Random _random = new Random();
            if (czyMalaDuzaLitera)
                charSet += maleLitery;
                charSet += duzeLitery; 
            if (czyCyfry)
                charSet += cyfry;
            if (czyZnakiSpecjalne)
                charSet += znakiSpecjalne;
            for (int i = 0; i < length; i++)
                haslo[i] = charSet[_random.Next(charSet.Length - 1)];
            return string.Join(null, haslo);
        }
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show(GenerujHaslo(checkBox1.IsChecked == true, checkBox2.IsChecked == true, checkBox3.IsChecked == true, int.Parse(ileZnakowInput.Text)));
        }
        private void buttonZatwierdz_Click(object sender, RoutedEventArgs e)
        {
            string messageBoxText = $"Dane pracownika: {ImieInput.Text} {NazwiskoInput.Text}, {StanowiskoComboBox.Text}. Hasło: {GenerujHaslo(checkBox1.IsChecked == true, checkBox2.IsChecked == true, checkBox3.IsChecked == true, int.Parse(ileZnakowInput.Text))}";
            MessageBox.Show(messageBoxText);
        }
    }
}
