we'll explore the intriguing realm of 
 optimizing performance by breaking down Directed Acyclic Graphs (DAGs) into stages. Our objective is
 to grasp how this technique significantly boosts the execution speed of PySpark applications.

 Why Break Down DAG into Stages:

 Breaking down the DAG into stages is crucial for optimizing PySpark performance, offering better parallelization
  and optimization. By efficiently leveraging available CPU cores, fine-tuning the number of partitions 
 ensures a balanced workload distribution. This technique proves especially beneficial when tackling large datasets
 and complex transformations, resulting in an overall enhancement of application speed.

 Breaking a PySpark DAG (Directed Acyclic Graph) into stages also improves performance by optimizing the execution plan.
 A DAG comprises transformations and actions on a DataFrame, where each stage represents a unit of work executed 
 on a single node. This optimization minimizes data shuffling between nodes and maximizes resource utilization.


 what is the scenario :
  we initiate a SparkSession, load sample data into a DataFrame, 
 and determine the number of available cores . 
 We then adjust the number of partitions based on a percentage of available cores (in this case, 80%).
 This adjustment proves instrumental in improving Spark job performance by minimizing data shuffling during transformations.
