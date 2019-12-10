using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Utilities : MonoBehaviour
{
    //1. Code that moves an AI around. This uses code to move an AI
    //that is set up as a navmesh agent to move from one navigation 
    //point to the next.
    public void GetNextNavPoint()
    {
        //Moves one more up the path count
        pathCount = (pathCount + 1);
        //If this code is past the maximum nav point then reset to
        //the first navpoint
        if (pathCount >= path.Length)
        {
            pathCount = 0;
        }
        //Send the AI to the new navpoint
        ai.SetTarget(path[pathCount].transform);
    }

    //2. Code that detects collision for an AI and then checks if the
    //collision was tagged as a bullet and if it is it destroys the
    //AI
    public void OnCollisionEnter(Collision collision)
    {
        //Check if collision object is tagged as bullet
        if (collision.gameObject.tag == "Bullet")
        {
            //Destroys this game object
            Destroy(this.gameObject);
        }
    }

    //3. Sets up a state machine AI
    void Start()
    {
        //Accesses the AI character controller for the AI
        ai = GetComponent<UnityStandardAssets.Characters.ThirdPerson.AICharacterControl>();
        //Sets starting state as patrol
        SetState(new PatrolState(this));
    }
    void FixedUpdate()
    {
        //This update calls the current states check transitions and 
        //act functions to keep it doing things
        currentState.CheckTransitions();
        currentState.Act();
    }
    //Sets the AI to the new state which is given when this function
    //is called
    public void SetState(State state)
    {
        //Checks if AI has a current state, and if it does calls that
        //states exit function
        if (currentState != null)
        {
            currentState.OnStateExit();
        }
        //Assigns the new state and sets the AI's name to show its
        //current state
        currentState = state;
        gameObject.name = "AI agent in state " + state.GetType().Name;
        //Calls the new states enter function if it is not null
        if (currentState != null)
        {
            currentState.OnStateEnter();
        }
    }

    //4. Handles player death and respawning.
    //Checks for collision
    public void OnCollisionEnter(Collision collision)
    {
        //Checks if collision is tagged as bullet
        if (collision.gameObject.tag == "Bullet")
        {
            //Lowers the health counter and updates the health UI
            health--;
            healthCounter.text = health.ToString();
            //Checks if health hits 0 or below
            if (health <= 0)
            {
                //Reloads the main gameplay scene
                SceneManager.LoadScene("Main Game");
            }
        }
    }

    //5. Plays audio when bullet is spawned (aka when gun is fired).
    void Shoot
    {
        //Some unecessary code was here
        //This gets the spawned bullets audio source
        var audio : AudioSource = bullet.GetComponent(AudioSource);
        //Sets the audio source to not loop the sound clip
        audio.loop = false;
        //Plays the attached sound clip
        audio.Play();
    }

}
