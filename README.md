## Lainez, Grand Vince J.   BSCS 3B


### LEVEL 1: (4 points each)

 1. Differentiate between SIMD and MIMD? Explain.

    SIMD or the Simple Instruction Multiple Data stream and MIMD or Multiple Instructions Multiple Data stream are some of the classifications of Flynn’s Taxonomy. Although they both works on different or multiple data streams, they have a big difference. SIMD only executes one instructions in every data streams, this means that the system will only do one job whatever the type of data is streamed to it. MIMD on the other hand, executes multiple instructions in multiple data streams. This architecture consists of a group of N-individual, closely connected processors. Each CPU has memory that can be shared by all processors but is inaccessible to the other processors directly and it also includes processors that operate independently and asynchronously. Various processors may be carrying out various instructions at any time on various pieces of data.

 4. Explain what pipelining is.

    Pipelining is the breaking of task into steps executed in different processor or cores. It is the procedure of adding up instructions received from the processor via a pipeline. It enables the systematic storing and execution of instructions. Processing in a pipeline is another name for it. Pipelining is a technique that overlaps several instructions as they are being executed. It is comparable to an assembly line of a factory in production, where many product parts are put together simultaneously, however eventually some elements would need to go together before others. The total process can benefit from those operations that can run concurrently even if there is some sequential dependency. This can be considered as a type of parallel of computing with different steps are executed on multiple cores with the numbers data streaming through.
   
 5. Illustrate and explain what a Von Neuman Architecture is.

   ![image](https://user-images.githubusercontent.com/82772962/181340964-097b36e3-5cd6-4896-8fde-05da32270208.png)

   Von Neumann Architecture as we can see in the figure above, is a computer architecture based on 1945 defined by John Von Neumann. The foundation of modern computers is the stored program paradigm, in which data and programs are stored separately in memory units and treated equally. It is a stored-program computer in which a fetch of instructions and simultaneous execution of data operations are not possible. It is primarily separated into three fundamental units: the Input and Output device, the Central Processing Unit(CPU) and the Primary Memory Unit. 
    This model starts with the input device that sends data or instructions to be executed. After that, the data will be process in the CPU or in the processor. As we can see the Central Processing Unit is divided into two units, the control unit which handles the processor's control signals and the arithmetic/logic unit or ALU which performs the different calculations and operations. The memory unit  includes: accumulator, which accumulates the results of calculations conducted by the Arithmetic/Logic Unit (ALU); and Program Counter, which monitors the location in memory of the upcoming instructions. The computer then sends the following address to the memory address register (MAR).  Memory Address Register: This register keeps track of where in memory instructions need to be stored or fetched from. • Memory Data Register: This register keeps track of instructions that have been read from memory as well as any data that needs to be sent to and kept in memory. The most recently acquired instructions are kept in the current instruction register while they wait to be translated and executed, while the instructions that won't be processed right away are put in the instruction buffer register.
   After the data has been processed, the data will be displayed in Output devices in a human readable format.
   
### LEVEL 2: (5 points each)

 2. In a right triangle, the square of the length of one side is equal to the sum of the squares of the lengths of the other two sides. Write a program that prompts the user to enter the length of the three sides of a triangle and then outputs a message indicating whether the triangle is a right triangle.

    CODE:

      [L2_Item2.py](https://github.com/yab0ku/FinalExam/blob/b8c4ae4481f85987701fdfe95d3276363dbaf0d6/FinalExam/L2_Item2.py)

    OUTPUT:

      ![image](https://user-images.githubusercontent.com/82772962/181364760-3ec13d9b-eadf-4d8c-93cf-234bdcc2d7c1.png)

 3. Write a program that prompts the user to input a number between 0 and 35. If the number is less than or equal to 9, the program should output the number; otherwise, it should output A for 10, B for 11, C for 12… and Z for 35.

    CODE:

      [L2_Item3.py](https://github.com/yab0ku/FinalExam/blob/e6e015868366bfa8000d5d090d9ac32f53b1a20e/FinalExam/L2_Item3.py)

    OUTPUT:

      ![image](https://user-images.githubusercontent.com/82772962/181289836-4e6a70f8-b2a8-4024-85fb-292de193e3d1.png)

 4. Write a program that will display all numbers divisible by 3, 4 and 5 from 1-50.

    CODE:

      [L2_Item4.py](https://github.com/yab0ku/FinalExam/blob/6a9c6d68547c3d59131373d732ae6aa2ff85f239/FinalExam/L2_Item4.py)

    OUTPUT:

      ![image](https://user-images.githubusercontent.com/82772962/181294301-eb781c81-a620-4978-bfc5-b5f8bccea675.png)


### LEVEL 3: (6 points each, +2 points if you get 2 LEVEL 3 questions correct.)

 1. Differentiate between Multiprocessing and Multithreading. Explain.

    Multiprocessing is a system or that works on two or more processors. Multiple CPUs are added to the system in order to boost the computing speed of the system. As a result of that, various executions and multiple processes are executed simultaneously and it is divided into two categories, symmetric and asymmetric multiprocessing. Symmetric Multiprocessing utilizes computer hardware and software that consists of two or more processors that are similar and coupled by a single memory space. These processors are treated equally and have full access to all input and output devices while in Asymmetric Multiprocessing, the access to distinct input and output (I/O) devices is available to various CPUs. For instance, one CPU might handle I/O tasks while another might concentrate on OS upkeep.
   
    Multithreading is a programming method that gives different code snippets to different processes. These threads of code execute simultaneously and in parallel with one another. Within a parent process, these threads share the same memory area. This decreases system memory usage, speeds up computation, and enhances application performance. We can illustrate this by having several browser tabs open when using your computer and conducting an internet search. Additionally, you might be using a desktop program to listen to music. Even though they are both running at the same time, the internet browser and the music app are two separate processes. Although your internet browser is the parent process, the numerous tabs you have open while exploring the web represent threads of that process.
   
    In conclusion, while multithreading employs a single process with several code segments to boost computing capacity, multiprocessing makes advantage of two or more CPUs to do so.
   
 2. Explain the difference between Serial Computing and Parallel Computing.

    Serial computing is a type of processing where there are only one processor performing. This is a type of processing in which the tasks are completed one at a time and done in a sequential order. Data transfers in a bit a bit format so it requires more time to complete a task thus the work load of the processor is high. Parallel computing on the other hand, uses multiple processors meaning we can do and complete the different tasks at the same time. We divide the tasks and distribute it into the multiple processors in order to boost the execution time and to lessen the load of the processors. We can therefore conclude that parallel computing can give higher performance, faster computation and can finish more task in a period of time than the serial computing.

 3. Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none. If the second parameter is "asc," then the function should return a list with the numbers in ascending order. If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.

    CODE:

      [L3_Item3.py](https://github.com/yab0ku/FinalExam/blob/524801c543fcb0cedf3d9c48307a66054ae954af/FinalExam/L3_Item3.py)

    OUTPUT:

      ![image](https://user-images.githubusercontent.com/82772962/181302104-1cb033c8-a971-4db5-bd84-f77565c97998.png)
      
### LEVEL 4: (10 points each)

1. Write a program that will generate 100 3-digit random numbers and store it in a list. The program should display the following:

      a. All elements in the list
      
      b. All numbers grouped by odd and even numbers
      
      c. All numbers divisible by 9.
      
      d. All prime numbers
      
      e. All numbers that contains the digit 9 (e.g 29, 91, 393, 961)

   CODE:
   
   [L4_Item1.py](https://github.com/yab0ku/FinalExam/blob/e4528bfa9cc40fcadb18936a6d27bfaf9865ed3a/FinalExam/L4_Item1.py)
   
   OUTPUT:
   
   ![image](https://user-images.githubusercontent.com/82772962/181373355-41001cc6-ea3f-4dbb-b301-e429592201f5.png)


