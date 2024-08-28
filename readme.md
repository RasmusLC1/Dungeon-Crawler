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

    Algorithm Optimization: Efficient sorting, searching, and pathfinding algorithms.
    Memory Management: Use of memory-efficient data structures.
    Lazy Loading: Loading resources only when needed to reduce memory footprint.
    Location detection for physics objects to only interract with nearby objects

    
Algorithms used:

    Raycasting: used for efficient lighting engine and line of sight
    A* Pathfinding: Used for efficient pathfinding around the dungeon by enemies
    Location Based Collision Detection: Used for efficiently computing collisions
    Collision Layers: used to seperate collision detection so that an entity only checks for collision with relevant objects
    Tilemap: used to generate and manage dungeon
    Built in Timsort: for sorting object in O(n log n) time
    Animation Interpolation: For handling depth of field and general animation quality
    


