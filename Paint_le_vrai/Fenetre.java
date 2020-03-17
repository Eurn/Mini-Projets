
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.util.*;
import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.JOptionPane;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.JTabbedPane;

public class Fenetre extends JFrame
{
  private JPanel general;
  private Dessin dessin;
  private String forme;
  private int x;
  private int y;
  private boolean first_clic=false;
  private boolean second_clic=false;
  private int old_x;
  private int old_y;
  private int old_x_2;
  private int old_y_2;
  private int rayon;
  private int rayon2;
  private Vue zone;
  private JPanel jp; //panel nord
  private JPanel pannel_sud;
  private JButton b_select;
  BoutonListener blis=new BoutonListener();
  private JTabbedPane onglets;
  private JButton remplis;
  private boolean remplissage=false;
  private Color couleur;
  private JColorChooser tcc;
  private Crayon cray=new Crayon(0,0,couleur);
  private Gomme gomme=new Gomme();
  private int taille_gomme=50;
  private JPanel panel_text;
  private JTextArea texte;
  private String text2;

  public Fenetre(Dessin dessin)
  {
    super("test");
    //KeyListener klis=new ClavierListener();
    //this.addKeyListener(klis);
    //this.setFocusable(true);
    //this.requestFocus();
    this.dessin=dessin;
    this.setSize(800,600);
    this.initialise();
    this.setVisible(true);
    this.setDefaultCloseOperation(EXIT_ON_CLOSE);
    this.setResizable(true);
  }

  public void initialise()
  {
    onglets=new JTabbedPane();

    general=new JPanel();
    general.setLayout(new BorderLayout());
    initPanelNord();
    general.add(jp,BorderLayout.NORTH);

    initPanelSud();
    general.add(pannel_sud,BorderLayout.SOUTH);


    zone=new Vue(dessin);
    CurseurListener mlis=new CurseurListener();
    zone.addMouseListener(mlis);
    MouveMouseListener mml=new MouveMouseListener();
    zone.addMouseMotionListener(mml);

    general.add(zone,BorderLayout.CENTER);


    initPanelText();

    onglets.add("General",general);
    onglets.add("Texte",panel_text);
    onglets.add("Couleurs",initPanelDroite());

    this.add(onglets);

    dessin.add(gomme);
  }

  public void actualiser()
  {
    zone=new Vue(dessin);
    b_select.setBackground(null);
    repaint();
  }

  public void initPanelText()
  {
    panel_text=new JPanel();
    panel_text.setLayout(new BorderLayout());

    JButton text=new JButton("Valider");
    text.addActionListener(blis);

    texte=new JTextArea();
    panel_text.add(texte,BorderLayout.CENTER);

    panel_text.add(text,BorderLayout.SOUTH);
  }

  public JPanel initPanelDroite()
  {
    JPanel couleurs=new JPanel();

    tcc= new JColorChooser();
    CouleurListener cl=new CouleurListener();
    tcc.getSelectionModel().addChangeListener(cl);
    tcc.setBorder(BorderFactory.createTitledBorder("Choisissez votre couleur"));
    couleurs.add(tcc);
    return couleurs;
  }

  public void initPanelSud()
  {
	pannel_sud=new JPanel();;

    JButton s=new JButton("Segment");
    s.addActionListener(blis);
    pannel_sud.add(s);
    
    JButton t=new JButton("Triangle");
    t.addActionListener(blis);
    pannel_sud.add(t);

    JButton r=new JButton("Rectangle");
    r.addActionListener(blis);
    pannel_sud.add(r);

    JButton c=new JButton("Cercle");
    c.addActionListener(blis);
    pannel_sud.add(c);

    JButton e=new JButton("Ellipse");
    e.addActionListener(blis);
    pannel_sud.add(e);
  }

  public void initPanelNord()
  {
    jp=new JPanel();

    JButton crayon=new JButton("Crayon");
    crayon.addActionListener(blis);
    jp.add(crayon);

    remplis=new JButton("Remplissage");
    remplis.addActionListener(blis);
    jp.add(remplis);

    JButton del=new JButton("Supprimer");
    del.addActionListener(blis);
    jp.add(del);
    
    JButton retour = new JButton("Retour");
    retour.addActionListener(blis);
    jp.add(retour);
    
    JButton gomme=new JButton("Gomme");
    gomme.addActionListener(blis);
    jp.add(gomme);
  }



  class CurseurListener extends MouseAdapter
  {
    int pos_x;
    int pos_y;
    int rayon;
    public void mouseClicked(MouseEvent e)
    {
      if(forme!=null)
      {
        x=e.getX();
        y=e.getY();
        switch(forme)
        {
          case "Cercle":
            if(!first_clic)
            {
              old_x=x;
              old_y=y;
              first_clic=true;
            }else
            {
              pos_x=old_x;
              pos_y=old_y;
              rayon=Math.abs(x-old_x);
              if(old_x>x)
              {
                pos_x=x;
              }
              if(old_y>y)
              {
                pos_y=y;
              }
              dessin.add(new Cercle(pos_x,pos_y,rayon,remplissage,couleur));
              forme=null;
              first_clic=false;
              actualiser();
            }
            break;

          case "Rectangle":
            if(!first_clic)
            {
              old_x=x;
              old_y=y;
              first_clic=true;
            }else
            {
              dessin.add(new Rectangle_mine(old_x,old_y,x,y,remplissage,couleur));
              first_clic=false;
              forme=null;
              actualiser();
            }
            break;

          case "Triangle":
            if(!first_clic)
            {
              old_x=x;
              old_y=y;
              first_clic=true;
            }else if(!second_clic)
            {
              old_x_2=x;
              old_y_2=y;
              second_clic=true;
            }else
            {
              dessin.add(new Triangle(old_x,old_y,old_x_2,old_y_2,x,y,remplissage,couleur));
              first_clic=false;
              second_clic=false;
              forme=null;
              actualiser();
            }
            break;

          case "Ellipse":
            if(!first_clic)
            {
              old_x=x;
              old_y=y;
              first_clic=true;
            }else
            {
              rayon=Math.abs(x-old_x);
              rayon2=Math.abs(y-old_y);
              if(old_x>x)
              {
                old_x=x;
              }
              if(old_y>y)
              {
                old_y=y;
              }

              dessin.add(new Ellipse(old_x,old_y,rayon,rayon2,remplissage,couleur));
              first_clic=false;
              forme=null;
              actualiser();
            }
            break;

          case "Segment":
            if(!first_clic)
            {
              old_x=x;
              old_y=y;
              first_clic=true;
            }else
            {
              dessin.add(new Segment(old_x,old_y,x,y,couleur));
              first_clic=false;
              forme=null;
              actualiser();
            }
            break;
          case "Crayon":
            forme=null;
            cray.Crayon_add(null);
            break;

          case "Texte":
            forme=null;
            dessin.add(new Texte(x,y,couleur,text2));
            actualiser();
            break;
        }
      }

    }
  }

  class MouveMouseListener implements MouseMotionListener
  {
    java.awt.Point mp;
    boolean ajouter=false;

    public void mouseDragged(MouseEvent med)
    {
      if(forme=="Crayon")
      {
        if(!ajouter)
        {
          cray.set_color(couleur);
          dessin.add(cray);
          ajouter=true;
        }
        mp=med.getPoint();
        cray.Crayon_add(new Point((int)mp.getX(),(int)mp.getY()));
        dessin.add(cray);
        actualiser();
      }else if(forme=="Gomme")
      {
        mp=med.getPoint();
        ArrayList<Cercle> gommes=new ArrayList<Cercle>();
        gommes.add(new Cercle((int)mp.getX(),(int)mp.getY(),taille_gomme,true,null));
        //gomme.Gomme_add((int)mp.getX(),(int)mp.getY(),taille_gomme);
        dessin.add(new Gomme(gommes));
        actualiser();
      }
    }
    public void mouseMoved(MouseEvent med2){}

    public void mouseExited(MouseEvent e){}
  }

  /*class ClavierListener implements KeyListener
  {
    public void keyReleased(KeyEvent e){}

    public void keyTyped(KeyEvent e){}

    public void keyPressed(KeyEvent e)
    {
      System.out.println("press");
      int touche=e.getKeyCode();
      System.out.println(touche);
      boolean ok=false;
      switch(touche)
      {
        case KeyEvent.VK_C:
          forme="Cercle";
          System.out.println("Cercle press");
          ok=true;

        case 'r':
          forme="Rectangle";
          ok=true;

        case 'e':
          forme="Ellipse";
          ok=true;

        case 't':
          forme="Triangle";
          ok=true;

        case 's':
          forme="Segment";
          ok=true;
      }

      if(ok)
      {
        if(b_select!=null)
        {
          //b_select.setBackground(null);
        }
      }
    }
  }*/

  class BoutonListener implements ActionListener
  {
    public void actionPerformed(ActionEvent e)
    {
      String commande=e.getActionCommand();
      if(commande=="Remplissage")
      {
        if(remplissage)
        {
          remplissage=false;
          remplis.setBackground(null);
        }else
        {
          remplissage=true;
          remplis.setBackground(couleur);
        }
      }else
      {
        if(b_select!=null)
        {
          b_select.setBackground(null);
        }
        b_select=(JButton)e.getSource();
        b_select.setBackground(Color.RED);
        forme=commande;
      }

      if(commande=="Retour")
      {
        dessin.remove(dessin.size()-1);
        actualiser();
      }
      if(commande=="Supprimer")
      {
        dessin.clear();
        actualiser();
      }
      if(commande=="Valider")
      {
        text2=texte.getText();
        forme="Texte";
      }
    }
  }

  class CouleurListener implements ChangeListener
  {
    public void stateChanged(ChangeEvent cou)
    {
      couleur=tcc.getColor();
      if(remplissage==true)
      {
        remplis.setBackground(couleur);
      }
    }
  }

}
