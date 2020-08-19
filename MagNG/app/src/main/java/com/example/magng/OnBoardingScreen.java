package com.example.magng;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager2.widget.ViewPager2;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;

import java.util.ArrayList;
import java.util.List;

public class OnBoardingScreen extends AppCompatActivity {
    private OnboardingAdapter onboardingAdapter;
    ImageButton imageButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_on_boarding_screen);

        ViewPager2 onboardingViewPager = findViewById(R.id.onboardingViewPager);
        onboardingViewPager.setAdapter(onboardingAdapter);
        imageButton = findViewById(R.id.imageButton);

        //button to open the sign in page when clicked
        imageButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(OnBoardingScreen.this, MainActivity.class);
                startActivity(intent);
            }
        });
    }

    private void setupOnboardingItems(){
        List<OnboardingItem> onboardingItems = new ArrayList<>();

        // onboard screen details
        OnboardingItem onboardingMessage = new OnboardingItem();
        onboardingMessage.setTextDescription("Share your magazines, with friends and family, see what others are reading.");
        onboardingMessage.setImage(R.drawable.onboard_image);

        // onboard Magazine screen
        OnboardingItem onboardMagazine = new OnboardingItem();
        onboardMagazine.setTextDescription("Magazines at your finger tips. Easily access your magazines anywhere any time across all devices.");
        onboardMagazine.setImage(R.drawable.message_icon);

        OnboardingItem onboardingNotification = new OnboardingItem();
        onboardingNotification.setTextDescription("Explore and enjoy thousands of magazines. Read your magazines online or download them for offline reading.");
        onboardingNotification.setImage(R.drawable.lens_icon);

        onboardingItems.add(onboardingMessage);
        onboardingItems.add(onboardingNotification);
        onboardingItems.add(onboardMagazine);

        onboardingAdapter = new OnboardingAdapter(onboardingItems);


    }

}