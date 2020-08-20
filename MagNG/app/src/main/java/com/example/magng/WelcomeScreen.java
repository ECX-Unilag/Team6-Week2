package com.example.magng;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

public class WelcomeScreen extends AppCompatActivity {
    private ImageView welcomeScreen;
    private static int splashTimeOut = 5000;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_welcome_screen);

        welcomeScreen = findViewById(R.id.welcomeScreen);

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent intent = new Intent(WelcomeScreen.this, MainActivity.class);
                startActivity(intent);
                finish();
            }
        }, splashTimeOut);

        // create an animation to display the splash screen
        Animation myanim = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.splashanimation);
        welcomeScreen.startAnimation(myanim);
    }
}