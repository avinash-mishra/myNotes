class Constructor {
    private String name;
    private int id;
    private String department;
    private String position;

    public Constructor(){
        this.name="(not set)";
        this.id = 0;
        this.department = "(not set)";
        this.position = "(not set)";
    }

    public Constructor(String name, int id ){
        this.name=name;
        this.id = id;
        this.department = "(not set)";
        this.position = "(not set)";
    }

    public Constructor(String name, int id, String department, String position){
        this.name=name;
        this.id = id;
        this.department = department;
        this.position = position;
    }

    public static void printInfo(Constructor e)
    {
        System.out.println(e.getName() + ", " + e.getIdNumber() + ", " + e.getDepartment() + ", " + e.getPosition());
    }

    public static void main(String[] args)
    {
        Constructor e1 = new Constructor();
        Constructor e2 = new Constructor("Bill Gates", 1975);
        Constructor e3 = new Constructor("Steve Jobs", 1976, "Design", "Engineer");

        printInfo(e1);
        printInfo(e2);
        printInfo(e3);
    }

    protected static String getName(Constructor e){
        return e.name;
    }

    protected static int  getIdNumber(Constructor e){
        return e.id;
    }

    protected static String  getDepartment(Constructor e){
        return e.department;
    }

    protected static String  getPosition(Constructor e){
        return e.position;
    }

}
