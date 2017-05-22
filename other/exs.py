public class NestedIterator implements Iterator<Integer> {

    public List<NestedInteger> nestedList;
    private int next=0;
    private int nextNested=0;
     boolean hasNext=false;
      boolean hasNextNext=false;
     NestedIterator nextIterator=new NestedIterator();
    public NestedIterator(List<NestedInteger> nestedList) {
        this.nestedInteger=nestedList;
    }
    public NestedIterator(){}

    @Override
    public Integer next() {
        Integer i;
        if(hasNextNext){
           i= nextIterator.next();
        }else{
            i=nestedList.get(next);
            next++; 
        }
       

        return i;
        
    }

    @Override
    public boolean hasNext() {
        
        if(nestedList.get(next).isInterger()){
            hasNext=true;
            hasNextNext=false;
        }else{
           
           nextIterator.nestedList=nestedList.get(next);
            hasNextNext=nextIterator.hasNext();
            if(!hasNextNext){
                next++;
                
            }

        }

        return hasNext;
    }
}


public class Solution {
    private List<Integer> result=new ArrayList<>();
    public int[] findOrder(int numCourses, int[][] prerequisites) {

        if (prerequisites.length>0) {
            
            result.add(prerequisites[0][1]);
            result.add(prerequisites[0][0]);
            
        }
        if (prerequisites.length>1) {
             for (int i=1;i<prerequisites.length ;i++ ) {
                int p=findPosition(prerequisites[i][1]);
                insert(p,prerequisites[i][0]);
                          
            }
            
        }

       return listToArray(result);
        
    }


    public int findPosition(int value){
        return result.indexOf(value);
    }

    public void insert(int p,int value){
        int p2=p+1;
        result.add(p2,value);
    }

    public int[] listToArray(List<Integer> list){
        int[] array=new int[list.size()];
        for (int i=0;i<array.length ;i++ ) {
            array[i]=list.get(i).intValue();
        }
        return array;
    }
}