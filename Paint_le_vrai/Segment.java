
import java.awt.Color;
public class Segment extends Rectangle_mine
{
  public Segment(int x,int y,int p1_x,int p1_y,Color color)
  {
    super(x,y,p1_x,p1_y,false,color);
    this.vue=new Dessin_Segment(this);
  }

  public String type()
  {
    return "Segment";
  }
}
