# AI Checkers Coach

An AI-powered checkers project built from scratch in Python.

The goal is to start with a fully functional checkers game engine and gradually turn it into a machine-learning system that can analyze positions, evaluate moves, identify mistakes, and eventually act as a checkers coach.

## Project Goal

This project will be developed in stages:

1. Build a checkers board and piece system.
2. Implement all legal checkers moves.
3. Implement captures, multiple jumps, and king promotion.
4. Build a playable checkers game engine.
5. Implement a traditional AI using Minimax and Alpha-Beta pruning.
6. Use the traditional AI to generate training data.
7. Train a machine-learning model to evaluate checkers positions.
8. Use the ML model to evaluate and rank possible moves.
9. Build an AI Checkers Coach that can:
   - Analyze a player's moves.
   - Identify mistakes and blunders.
   - Explain why a move was good or bad.
   - Suggest a better move.
   - Track a player's performance over multiple games.
10. Eventually experiment with neural networks and self-play.

The project is intentionally being built from the ground up so that the machine-learning portion is connected to a real working system rather than being a standalone ML exercise.

---

# Rules

## Checkers Variant

This project will use **American Checkers**, also known as **English Draughts**.

We will NOT use the rules of International Draughts.

### Board

- Board size: 8 × 8.
- Only the 32 dark squares are playable.
- Each player starts with 12 pieces.
- Pieces are initially placed on the three rows closest to each player's side.

### Players

There are two players:

- Black
- White

Black will move first.

---

# Pieces

Each player starts with regular pieces called **men**.

A piece can become a **king** after reaching the opponent's back row.

### Regular Piece

A regular piece:

- Moves diagonally forward by one square.
- Captures diagonally forward.
- Cannot move backward unless it has become a king.

### King

A king:

- Moves diagonally forward or backward by one square.
- Can capture forward or backward.

Kings in this project are **not flying kings**.

That means a king can move only one square at a time and cannot travel across multiple empty squares like it can in International Draughts.

---

# Captures

Capturing is mandatory.

If a player has at least one legal capture available, they MUST make a capture instead of making a normal move.

For example:

```text
Normal move available
Capture available
        ↓
   Capture MUST
   be played
```

### Capturing a Piece

A piece captures an opponent's piece by:

1. Moving diagonally over the opponent's piece.
2. Landing on the empty square immediately beyond it.
3. Removing the captured piece from the board.

---

# Multiple Captures

If, after making a capture, the same piece can make another capture, the player must continue capturing with that piece.

Example:

```text
Capture → Capture → Capture
```

The entire sequence is considered one move.

The player cannot stop a multiple-capture sequence voluntarily when another capture is available.

---

# Promotion

When a regular piece reaches the opponent's back row, it becomes a king.

Example:

```text
Regular Piece
     ↓
Reaches last row
     ↓
    King
```

A king can subsequently move and capture both forward and backward.

For this project, promotion happens when the piece reaches the king row during its move.

---

# Winning

A player wins when their opponent:

- Has no pieces remaining, OR
- Has no legal moves available.

Therefore, a player can lose either by having all of their pieces captured or by being completely unable to move.

---

# Draws

For the initial version of the project, we will keep draw detection simple.

A game can be declared a draw when:

- The same position occurs three times, OR
- The game reaches a predefined move limit without meaningful progress.

The exact draw implementation can be refined when the game engine is complete.

---

# Board Representation

Internally, the board will use an 8 × 8 structure.

Empty squares will be represented by:

```python
None
```

Pieces will be represented using the `Piece` class.

A piece will contain information such as:

```python
Piece("black")
Piece("white")
Piece("black", is_king=True)
Piece("white", is_king=True)
```

The visual representation will use:

```text
B = Black piece
W = White piece
b = Black king
w = White king
. = Empty square
```

---

# AI Architecture

The project will use multiple stages of AI rather than immediately jumping into machine learning.

## Stage 1 — Checkers Engine

Build:

- Board
- Pieces
- Moves
- Legal move generation
- Captures
- Multiple captures
- King promotion
- Win/draw detection

## Stage 2 — Traditional AI

Implement:

- Minimax
- Alpha-Beta pruning
- Position evaluation

The traditional AI will act as our initial "teacher".

## Stage 3 — Training Dataset

Generate thousands of checkers positions using the game engine and traditional AI.

Each position can contain information such as:

```text
Board position
Side to move
Possible moves
Position evaluation
Best move
```

This data will be used to train machine-learning models.

## Stage 4 — Machine Learning

Train a model to estimate the value of a position.

The eventual goal is for the ML model to learn something similar to:

```text
Board position
      ↓
ML Model
      ↓
Position evaluation
```

We can then evaluate different possible moves:

```text
Current position
       ↓
Generate legal moves
       ↓
Evaluate resulting positions
       ↓
Rank moves
       ↓
Best move
```

## Stage 5 — AI Checkers Coach

The final system will be able to analyze a player's game.

For example:

```text
Player's move
     ↓
Analyze position
     ↓
Compare with AI evaluation
     ↓
Detect mistake
     ↓
Suggest better move
     ↓
Explain the position
```

The coach should eventually be able to identify things such as:

- Good moves
- Mistakes
- Blunders
- Missed captures
- Missed opportunities
- Losing material
- Poor positioning
- King opportunities

---

# Technology

The initial project will be built using Python.

Potential technologies:

- Python
- NumPy
- scikit-learn
- PyTorch
- Jupyter Notebook
- Matplotlib
- Git/GitHub

The project will prioritize free and open-source tools.

---

# Project Philosophy

This project is being built incrementally.

We will not immediately build a complicated neural network.

Instead:

```text
Checkers Rules
      ↓
Game Engine
      ↓
Traditional AI
      ↓
Training Data
      ↓
Machine Learning
      ↓
AI Coach
```

Each stage should work before moving to the next stage.

The final goal is not simply to make a checkers game.

The goal is to demonstrate the complete process of taking a real problem, building the underlying system, generating data, training an ML model, and turning the model into a usable AI application.