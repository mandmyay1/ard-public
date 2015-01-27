using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.Collections.Concurrent;

namespace WordsWithEnemies
{
    class Player
    {
        public int score = 0;
        public List<char> availableChars = null;
        public string word;

        protected WordsWithEnemiesGame refToGame;
        public Player(WordsWithEnemiesGame game)
        {
            refToGame = game;
        }

        public virtual void chooseWord()
        {
            word = getWord();
            while (!charsMakeUpWord(word) || !refToGame.isValidWord(word))
            {
                Console.Out.WriteLine("I am sorry but you cannot spell " + word + " with your letters. Try again.");
                word = getWord();
            }
            Console.Out.WriteLine("You chose " + word + " okay!");
        }
        private string getWord()
        {
            Console.Out.Write("Your letters: ");
            foreach( char c in availableChars )
            {
                Console.Out.Write(c);
                Console.Out.Write(" ");
            }
            Console.Out.Write("\nYour word ->");
            return Console.In.ReadLine();
        }
        protected bool charsMakeUpWord(string testWord)
        {
            List<char> copyChars = new List<char>(availableChars);
            foreach (char c in testWord)
            {
                if (copyChars.Contains(c))
                {
                    copyChars.Remove(c);
                }
                else
                {
                    return false;
                }
            }
            return true;
        }
    }

    class AI : Player
    {
        int difficulty;
        public AI(int diff, WordsWithEnemiesGame game): base(game)
        {
            difficulty = diff;
        }
        public override void chooseWord()
        {
            int maxLengthEncountered = 0;
            List<string> possibleWords = new List<string>();
            foreach (string validWord in refToGame.validWords)
            {
                if (charsMakeUpWord(validWord))
                {
                    /// Rules for difficulty: 
                    /// Difficulty 0 : 1-3 length words
                    /// Difficulty 1 : 1-5 length words
                    /// Difficulty 2 : 4+ length words
                    /// Difficulty 3 : Max-length words
                    if (difficulty == 0 && validWord.Length > 3) { continue; }
                    if (difficulty == 1 && validWord.Length > 5) { continue; }
                    if (difficulty == 2 && validWord.Length < 4) { continue; }
                    if (difficulty == 3 )
                    {
                        if(validWord.Length > maxLengthEncountered)
                        {
                            possibleWords.Clear();
                            maxLengthEncountered = validWord.Length;
                        }
                        else if (validWord.Length < maxLengthEncountered)
                        {
                            continue;
                        }
                    }
                    possibleWords.Add(validWord);
                }
            }
            possibleWords.Sort();
            word = possibleWords[refToGame.rand.Next(0, possibleWords.Count())];
            Console.Out.WriteLine("Player2 chose " + word + "!");
        }
    }

    class WordsWithEnemiesGame
    {
        public Random rand = new Random();
        List<char> weightedList;
        BlockingCollection<string> blockingCollection = new BlockingCollection<string>();
        public HashSet<string> validWords = new HashSet<string>();
        readonly int lengthOfCharArray = 12;
        readonly int maxScore = 10;
        int turn = 0;
        Player p1;
        Player p2;

        public WordsWithEnemiesGame(int difficulty)
        {
            weightedList = generateWeightedList();
            getValidWords();
            p1 = new Player(this);
            p2 = new AI(difficulty, this);
        }

        public void newTurn()
        {
            turn++;
            Console.Out.WriteLine("Turn " + turn + " -- Points You: " + p1.score + " Computer: " + p2.score);
            Console.Out.WriteLine("-------------------------------------------------------");
            List<char> turnWords = reshuffle();
            p1.availableChars = new List<char>(turnWords);
            p2.availableChars = new List<char>(turnWords);
            p1.chooseWord();
            p2.chooseWord();
            play();

        }

        private List<char> generateWeightedList()
        {
            char[] possibleCharacters = 
            {
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            };
            double[] biases = 
            {
                8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, //h
                0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, //r
                6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074 //z
            };
            List<char> weightedList = new List<char>();
            for (int i = 0; i < biases.Length; i++)
            {
                double multiples = biases[i] * 100;
                for (int j = 0; j < multiples; j++)
                {
                    weightedList.Add(possibleCharacters[i]);
                }
            }
            return weightedList;
        }
        public List<char> reshuffle()
        {
            List<char> retList = new List<char>();
            for (int i = 0; i < lengthOfCharArray; i++)
            {
                char c = weightedList[rand.Next(0,weightedList.Count())];
                retList.Add(c);
            }
            return retList;
        }

        private void getValidWords()
        {
            string site1 = @"http://www.joereynoldsaudio.com/enable1.txt";
            WebClient wc = new WebClient();
            wc.DownloadStringCompleted += new DownloadStringCompletedEventHandler(finishedDownloadingString);
            wc.DownloadStringAsync(new Uri(site1));
        }

        void finishedDownloadingString(object sender, DownloadStringCompletedEventArgs e)
        {
            string textFromSite = e.Result;
            string[] backslashRN = { "\r\n" };
            string[] words = textFromSite.Split(backslashRN, StringSplitOptions.RemoveEmptyEntries);
            for (int i = 0; i < words.Length; i++)
            {
                blockingCollection.Add(words[i]);
            }
            blockingCollection.CompleteAdding();
        }

        public bool isValidWord(string word)
        {
            foreach (string item in blockingCollection.GetConsumingEnumerable())
            {
                validWords.Add(item);
            }
            return validWords.Contains(word);
        }


        public void play()
        {

            string sortedWord1 = String.Concat(p1.word.OrderBy(c => c));
            string sortedWord2 = String.Concat(p2.word.OrderBy(c => c));

            StringBuilder leftover1 = new StringBuilder(), leftover2 = new StringBuilder();
            int pos1 = 0, pos2 = 0;
            while (pos1 < sortedWord1.Length && pos2 < sortedWord2.Length)
            {
                char c1 = sortedWord1[pos1];
                char c2 = sortedWord2[pos2];
                if (c1 == c2)
                {
                    pos1++;
                    pos2++;
                    continue;
                }
                else if (c1 < c2)
                {
                    leftover1.Append(c1);
                    pos1++;
                }
                else
                {
                    leftover2.Append(c2);
                    pos2++;
                }
            }
            while (pos1 < sortedWord1.Length)
            {
                leftover1.Append(sortedWord1[pos1]);
                pos1++;
            }
            while (pos2 < sortedWord2.Length)
            {
                leftover2.Append(sortedWord2[pos2]);
                pos2++;
            }
            string winner = p1.word + " vs " + p2.word + " -- ";
            if (leftover2.Length > leftover1.Length)
            {
                winner += "Player2 wins!";
            }
            else if (leftover1.Length > leftover2.Length)
            {
                winner += "Player1 wins!";
            }
            else
            {
                winner = "Tie game!";
            }
            //Console.Out.WriteLine("Player1 [" + leftover1.ToString() + "], Player2 [" + leftover2.ToString() + "] " + winner);
            Console.Out.WriteLine("Player1 has " + leftover1.Length + " letters left over - score " + leftover1.Length + " points.");
            Console.Out.WriteLine("Player2 has " + leftover2.Length + " letters left over - score " + leftover2.Length + " points.");
            p1.score += leftover1.Length;
            p2.score += leftover2.Length;
        }
        static void Main(string[] args)
        {
            Console.Out.WriteLine("Welcome to Words with Enemies!");
            Console.Out.Write("Select an AI difficulty\n"+
            "1) Easy\n2) Moderate\n"+
            "3) Challenging\n4) Impossible\n-->");
            string strDifficulty = Console.In.ReadLine();
            int iDifficulty = int.Parse(strDifficulty);
            Console.Out.Write("You have selected ");
            if (iDifficulty == 1) { Console.Out.Write("Easy"); }
            else if (iDifficulty == 2) { Console.Out.Write("Moderate"); }
            else if (iDifficulty == 3) { Console.Out.Write("Challenging"); }
            else if (iDifficulty == 4) { Console.Out.Write("Impossible"); }
            Console.Out.WriteLine("! - Let's begin!\n");

            WordsWithEnemiesGame game = new WordsWithEnemiesGame(iDifficulty-1); 
            while (game.p1.score < game.maxScore && game.p2.score < game.maxScore)
            {
                game.newTurn();
            }
            if (game.p1.score > game.p2.score)
            {
                Console.Out.WriteLine("Player1 wins the game with score " + game.p1.score);
            }
            else if (game.p2.score > game.p1.score)
            {
                Console.Out.WriteLine("Player2 wins the game with score " + game.p2.score);
            }
            else
            {
                Console.Out.WriteLine("Player1 and Player2 tie the game with score " + game.p2.score);
            }
        }
    }
}
