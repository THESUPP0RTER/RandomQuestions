import java.lang.Math.*;
public class Exercise09_09 {
    public static void main(String[] args) {
        RegularPolygon Polygon1 = new RegularPolygon();
        System.out.println("Polygon 1 perimeter: " + Polygon1.getPerimeter());
        System.out.println("Polygon 1 area: " + Polygon1.getArea());

        RegularPolygon Polygon2 = new RegularPolygon(6, 4);
        System.out.println("Polygon 2 perimeter: " + Polygon2.getPerimeter());
        System.out.println("Polygon 2 area: " + Polygon2.getArea());

        RegularPolygon Polygon3 = new RegularPolygon(10, 4, 5.6, 7.8);
        System.out.println("Polygon 3 perimeter: " + Polygon3.getPerimeter());
        System.out.println("Polygon 3 area: " + Polygon3.getArea());}
    static class RegularPolygon {
        /** Main method */
        private int n;
        private double side;
        private double x;
        private double y;
        public RegularPolygon() {
            n = 3;
            side = 1;
            x = 0;
            y = 0;
        }
        public RegularPolygon(int n, double side) {
            this.n = n;
            this.side = side;
        }
        public RegularPolygon(int n, double side, double x, double y) {
            this.n = n;
            this.side = side;
            this.x = x;
            this.y = y;
        }
        double getArea() {
            double Area = n * Math.pow(side,2) / (4 * Math.tan(Math.PI / n));
            return Area;
        }
        double getPerimeter() {
            double Perimeter = n * side;
            return Perimeter;
        }
    }
}
