Dungeon Crawler

A Python game focused on optimization and algorithmic implementation. The goal of this project is to maintain and develop a large and efficient codebase using Object-Oriented Programming (OOP) principles and design patterns. This game is built using the Pygame library.

This project implements several design patterns to ensure clean, maintainable code:

    Singleton: Used for global maintainability of the code structure
    Open-Closed: Used for expansion of physics entities without affecting the existing structure
    Substitution: Used for global management of physics entities
    Dependency Inversion: Used for global management to create global scalable functions
    Interface Segregation: Used to improve performance by removing reduncency in code
    Factory: Creates instances of various game objects dynamically.
    Strategy: Allows for interchangeable behaviors in game entities, such as different enemy AI strategies.
    Observer: Implements event-driven architecture for in-game events.
    Adapter: Used to manage all physics entities together
    Builder: Used to incrementally construct objects as their properties are needed
    Chain of responsibility: delegates tasks into various handlers depending on the specific context for optimisation
    Iterator: Iterate over relevant physics objects to determine what needs to be modified
    Mediator: Called handlers in the code delegates tasks
    
Optimization Techniques

To achieve high performance, the following optimization techniques have been used:

    Algorithm Optimization: Use of efficient sorting, searching, and pathfinding algorithms.
    Memory Management: Utilization of memory-efficient data structures.
    Lazy Loading: Loading resources only when needed to minimize memory usage.
    Location-Based Interaction: Physics objects only interact with nearby entities to reduce unnecessary computations.
    Code Refactoring: Regularly refactoring and iterating over code to enhance performance.
    Iterative Testing: Continuously testing for errors and optimizing performance.
    
Algorithms used:

    Raycasting: Efficiently calculates lighting and line of sight.
    A* Pathfinding: Optimizes enemy pathfinding around the dungeon.
    Location-Based Collision Detection: Efficiently computes collisions based on object locations.
    Collision Layers: Separates collision detection so that entities only check for collisions with relevant objects.
    Tilemap: Generates and manages the dungeon layout.
    Built-in Timsort: Sorts objects with O(n log n) time complexity for efficient processing.
    Animation Interpolation: Enhances depth of field and overall animation quality.
    


