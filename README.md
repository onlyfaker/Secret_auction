# Blind Auction Program

## 📋 Overview
This Blind Auction program is a simple command-line application that allows multiple users to submit sealed bids. The program keeps track of bids, clears the screen between entries, and determines the winner with the highest bid.

## ✨ Features
- Anonymous bidding system
- Supports multiple bidders
- Automatic highest bid detection
- Screen clearing between entries for privacy
- ASCII art logo for visual appeal

## 🛠 Requirements
- Python 3.x
- `art.py` file containing the LOGO variable

## 📦 Installation
1. Save the main script as `blind_auction.py`
2. Create `art.py` with the ASCII art logo
3. Ensure Python 3 is installed on your system

## 🚀 How to Run
```bash
python blind_auction.py
```

## 🎮 Usage Instructions
1. When prompted, enter your name
2. Enter your bid amount
3. Indicate if there are more bidders
4. If no more bidders, the program will reveal the winner

### Example Workflow
```
What is your name: Alice
What is your bid: $100
Are there any other bidders? Type 'yes' or 'no': yes

[Screen clears]

What is your name: Bob
What is your bid: $120
Are there any other bidders? Type 'yes' or 'no': yes

[Screen clears]

What is your name: Charlie
What is your bid: $110
Are there any other bidders? Type 'yes' or 'no': no

The winner is Bob with the highest bid 120
```

## 🧠 Program Logic
- Uses a dictionary `bids` to store bidder names and their bid amounts
- Clears screen between entries to maintain bid secrecy
- Finds the highest bid using a custom function
- In case of tied highest bids, the first received bid wins

## 📝 Key Functions
### `highest_bidder()`
- Iterates through bids dictionary
- Tracks and updates highest bid
- Determines and prints the winner

## 🔍 Bidding Rules
- Bids are anonymous
- First highest bid wins in case of a tie
- Bids are integers (whole dollar amounts)

## 💡 Potential Improvements
- Add bid validation
- Support decimal bid amounts
- Implement more robust tie-breaking mechanism
- Add error handling for non-integer inputs

## 🚧 Limitations
- No persistent storage of bids
- Simple console-based interface
- Requires manual entry of bids

## 📄 License
Open-source. Feel free to modify and distribute.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!
