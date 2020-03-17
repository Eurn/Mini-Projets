

import java.awt.Color;
public class Cercle extends Figure
{
  private int rayon;

  public Cercle(int x,int y,int rayon,boolean plein,Color color)
  {
    super(x,y,plein,color);
    this.vue=new Dessin_Cercle(this);
    this.rayon=rayon;
  }

  public int get_rayon()
  {
    return this.rayon;
  }

  public void set_rayon(int rayon)
  {
    this.rayon=rayon;
  }

  public String type()
  {
    return "Cercle";
  }
}